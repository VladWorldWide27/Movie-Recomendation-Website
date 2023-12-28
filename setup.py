from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Movie-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "Vladimir Deianov"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= "https://github.com/VladWorldWide27/Movie-Recomendation-Website.git",
    author_email="deyanovva@gmail.com",
    packages=[SRC_REPO],
    license="none",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
