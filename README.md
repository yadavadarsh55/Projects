# Real-Time Emotion Detection with Face Mesh

A Python application that performs real-time emotion detection using your webcam. The project combines MediaPipe's face mesh tracking with a deep learning model to detect seven different emotional states while displaying an elegant face mesh overlay.

## Features
* Real-time emotion detection (7 emotions)
   * Angry
   * Disgusted
   * Fearful
   * Happy
   * Neutral
   * Sad
   * Surprised
* Elegant face mesh visualization
* Bounding box detection
* Real-time emotion labeling
* Smooth 30% opacity mesh overlay
* Webcam support with 640x480 resolution
* Model evaluation tools with confusion matrix visualization

## Prerequisites
```
Python 3.7+
OpenCV (cv2)
TensorFlow
MediaPipe
NumPy
Matplotlib
scikit-learn
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/emotion-detection.git
cd emotion-detection
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
emotion_detection_project/
├── main.py                     # Main script to run real-time emotion detection
├── emotion_recognition_model_final.h5  # Pretrained model file
├── requirements.txt            # Lists all dependencies
├── README.md                   # Project description and usage instructions
└── LICENSE.md                  # Licensing information

```

## Usage

### Real-time Detection
1. Run the main application:
```bash
python main.py
```
2. Press 'f' to exit the application

## Model Architecture
The emotion detection model uses a CNN architecture:
* 4 Convolutional layers with max-pooling and dropout
* Dense layers for classification
* Trained on grayscale images (48x48 pixels)
* Evaluated using confusion matrix and classification metrics

## Configuration Options
You can modify these parameters in `main.py`:
```python
# Camera resolution
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Face detection confidence
min_detection_confidence=0.5

# Mesh overlay opacity
cv2.addWeighted(overlay, 0.3, img, 0.7, 0)  # 0.3 = 30% opacity
```

## Troubleshooting
1. **No webcam detected**:
   * Ensure your webcam is properly connected
   * Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if you have multiple cameras

2. **Model not found error**:
   * Verify that `emotion_recognition_model_final.h5` is in the `model/` directory

3. **Low performance**:
   * Reduce camera resolution
   * Ensure no other applications are using the webcam

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* FER2013 dataset from Kaggle used to train the model
* MediaPipe for the face mesh implementation
* TensorFlow for the deep learning framework
* OpenCV for computer vision capabilities
* scikit-learn for model evaluation metrics

## Author
Adarsh Yadav
* GitHub: @yadavadarsh55
* Email: adarshyadavsy@gmail.com

## Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Remember to star ⭐ this repository if you found it helpful!
