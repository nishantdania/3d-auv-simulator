/* 
	auv_gui.cpp
	A GUI for visualising the images and applying filters to it 
	Date created: November 2013 
	Author: Jason Poh & Lynnette Ng
*/


#include <QApplication>
#include <QFileDialog>
#include <QMessageBox>
#include <QImage>
#include <QPixmap>
#include <QDebug>

#include "vision_gui.h"
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/image_encodings.h>

#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <cv_bridge/cv_bridge.h>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "filters.h"

using namespace std;

enum camera_t { FRONT, BOTTOM };

//Utility functions declaration
QImage CvMatToQImage(const cv::Mat& mat);

//UI callback functions
void source_selected(int index);
void openFile(bool open);

class VisionUI {
private:
	ros::NodeHandle node;
	image_transport::ImageTransport it;
	image_transport::Subscriber sub1, sub2;

	FiltersContainer myFilters;
	FiltersContainer::Filters front_filters;
	FiltersContainer::Filters bottom_filters;
public:
	Ui::Vision ui;
	QMainWindow *window;

	VisionUI();
	void update_filter(camera_t camera, cv::Mat image);
	void change_front_topic(string topic);
	void change_bottom_topic(string topic);

	//ros callback functions
	void frontCameraCallback(const sensor_msgs::ImageConstPtr& msg);
	void bottomCameraCallback(const sensor_msgs::ImageConstPtr& msg);
};

//Global pointer to vision_ui to be used in callbacks
static VisionUI* vision_ui;

int main(int argc, char **argv) {
	ros::init(argc, argv, "auv_gui");

	//Initiate QAppication and UI
	QApplication app(argc, argv);

	VisionUI local_vision_ui;
	vision_ui = &local_vision_ui;

	//Events Handlers
	QObject::connect(vision_ui->ui.actionOpen, &QAction::triggered, openFile);
	QObject::connect(vision_ui->ui.source_ddm,
					 static_cast<void (QComboBox::*)(int)>(&QComboBox::currentIndexChanged),
					 source_selected);

	ros::AsyncSpinner spinner(4);
	spinner.start();

	return app.exec();
}

VisionUI::VisionUI() : it(node) {
	//Initialize filters
	front_filters = myFilters.getFrontFilters();
	bottom_filters = myFilters.getBottomFilters();

	//Initiate QAppication and UI
	window = new QMainWindow;
	ui.setupUi(window);
	window->setFixedSize(window->geometry().width(), window->geometry().height());
	for (int i = 0; i < front_filters.size(); i++)
		ui.frontfilter->addItem(QString::fromStdString(front_filters[i]->getName()));
	for (int i = 0; i < bottom_filters.size(); i++)
		ui.bottomfilter->addItem(QString::fromStdString(bottom_filters[i]->getName()));

	//Subscribe to ros topics
	change_front_topic("/front_camera/camera/image_raw");
	change_bottom_topic("/bot_camera/camera/image_raw");

	window->show();
}

void VisionUI::change_front_topic(string topic) {
	sub1 = it.subscribe(topic, 1, &VisionUI::frontCameraCallback, this);
}

void VisionUI::change_bottom_topic(string topic) {
	sub2 = it.subscribe(topic, 1, &VisionUI::bottomCameraCallback, this);
}

void VisionUI::frontCameraCallback(const sensor_msgs::ImageConstPtr& msg) {
	cv_bridge::CvImagePtr cv_ptr;
	cv::Mat smallerImage(ui.labelFront->size().height(), ui.labelFront->size().width(), CV_8UC3, cv::Scalar(0,0,0));

	try {
		cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::RGB8);
		cv::resize(cv_ptr->image, smallerImage, smallerImage.size());
	} catch (cv_bridge::Exception& e) {
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}

	ui.labelFront->setPixmap(QPixmap::fromImage(CvMatToQImage(smallerImage)));
	update_filter(FRONT, smallerImage);
}

void VisionUI::bottomCameraCallback(const sensor_msgs::ImageConstPtr& msg) {
	cv_bridge::CvImagePtr cv_ptr;
	cv::Mat smallerImage(ui.labelFront->size().height(), ui.labelFront->size().width(), CV_8UC3, cv::Scalar(0,0,0));
	try {
		cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::RGB8);
		cv::resize(cv_ptr->image, smallerImage, smallerImage.size());
	} catch (cv_bridge::Exception& e) {
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}

	ui.labelBottom->setPixmap(QPixmap::fromImage(CvMatToQImage(cv_ptr->image)));
	update_filter(BOTTOM, smallerImage);
}

void VisionUI::update_filter(camera_t camera, cv::Mat image) {
	Filter* f;
	switch (camera) {
		case FRONT: {
			f = front_filters[ui.frontfilter->currentIndex()];
			f->setInputImage(image);
			ui.labelFrontFiltered->setPixmap(QPixmap::fromImage(CvMatToQImage(f->getOutputImage())));
		}
			break;
		case BOTTOM: {
			f = bottom_filters[ui.bottomfilter->currentIndex()];
			f->setInputImage(image);
			ui.labelBottomFiltered->setPixmap(QPixmap::fromImage(CvMatToQImage(f->getOutputImage())));
		}
			break;
	}
	ros::Duration(0.15).sleep();
}

//UI Callbacks Definition

//Callback when data input source is changed from selection
//Just need to remap the topic
void source_selected(int index) {
	switch(index) {
	case 1: //Bag file must run uncompress bags
		vision_ui->change_front_topic("/front_camera/camera/image_raw");
		vision_ui->change_bottom_topic("/bot_camera/camera/image_raw");
		break;
	}
	vision_ui->change_front_topic("/front_camera/camera/image_raw");
	vision_ui->change_bottom_topic("/bot_camera/camera/image_raw");
}

void openFile(bool open) {
	QString selfilter = QString("BAG(*.bag)");
	QString filename = QFileDialog::getOpenFileName(vision_ui->window, QString("Open bag file"), QDir::currentPath(),
	QString("BAG files (*.bag);; All files (*.*)"), &selfilter);

	string filename_string = filename.toUtf8().constData();

	if (!filename_string.empty()){
		char command[256];
		snprintf(command, 256,
				 "gnome-terminal -e 'bash -c \"cd launch; roslaunch uncompressbags.launch bagfile:=%s; exec bash\" '",
				 filename_string.c_str());
		system(command);
	}

}

//Utility functions definition

QImage CvMatToQImage(const cv::Mat& mat) {
	// 8-bits unsigned, NO. OF CHANNELS=1
	if(mat.type() == CV_8UC1) {
		// Set the color table (used to translate colour indexes to qRgb values)
		QVector<QRgb> colorTable;
		for (int i = 0; i < 256; i++)
			colorTable.push_back(qRgb(i, i, i));
		// Copy input Mat
		const uchar *qImageBuffer = (const uchar*) mat.data;
		// Create QImage with same dimensions as input Mat
		QImage img(qImageBuffer, mat.cols, mat.rows, mat.step, QImage::Format_Indexed8);
		img.setColorTable(colorTable);
		return img;
	}
	// 8-bits unsigned, NO. OF CHANNELS=3
	if(mat.type() == CV_8UC3) {
		// Copy input Mat
		const uchar *qImageBuffer = (const uchar*)mat.data;
		// Create QImage with same dimensions as input Mat
		QImage img(qImageBuffer, mat.cols, mat.rows, mat.step, QImage::Format_RGB888);
		return img;
	} else {
		qDebug() << "ERROR: Mat could not be converted to QImage.";
		return QImage();
	}
}
