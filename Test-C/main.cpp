/* Below code is from the YT video */
#include <opencv2/opencv.hpp> // Says error, but it's not. It's b/c of intellisense
#include <iostream>

int main() {
    std::string imagePath = "someScreenshot.PNG";

    cv::Mat image = cv::imread(imagePath, cv::IMREAD_COLOR);
    cv::imshow("Display window", image);
    cv::waitKey(0);
    return 0;
}

/* Below code is the example from the OpenCV website */
// #include <opencv2/opencv.hpp>
// #include <iostream>
// using namespace cv;

// int main()
// {
//     std::string image_path = "someScreenshot2.PNG";
//     Mat img = imread(image_path, IMREAD_COLOR);

//     imshow("Display window", img);
//     int k = waitKey(0);

//     return 0;
// }


