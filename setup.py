import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='facenet-face-recognition',
    version='0.2',
    author="้ham",
    author_email="hamster.jargon@gmail.com",
    description="MTCNN + FaceNet -> Face Recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hamsterjar/face_verify.git",
    packages=setuptools.find_packages(),
    keywords=['facenet', 'opencv', 'deep learning', 'machine learning'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "opencv-python",
        "mtcnn",
        "sklearn",
        "tqdm",
        "numpy",
        "keras_facenet",
        "imutils",
        "tensorflow==2.4.0",
        "pandas"
    ]
)
