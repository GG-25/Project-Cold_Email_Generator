{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1AKsgBAJXezkS5DOzaitbMsk9QcVV2XqM",
      "authorship_tag": "ABX9TyPXWnU4Xy7VRsAhAUEPFfdo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GG-25/Project-Cold_Email_Generator/blob/main/Cold_Email_Generation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "nA5cSd2Ilaun",
        "outputId": "9bcd6959-796c-498c-c774-c9fc0a8ba587"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain\n",
            "  Downloading langchain-0.3.4-py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (6.0.2)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.0.36)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (3.10.10)\n",
            "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (4.0.3)\n",
            "Collecting langchain-core<0.4.0,>=0.3.12 (from langchain)\n",
            "  Downloading langchain_core-0.3.12-py3-none-any.whl.metadata (6.3 kB)\n",
            "Collecting langchain-text-splitters<0.4.0,>=0.3.0 (from langchain)\n",
            "  Downloading langchain_text_splitters-0.3.0-py3-none-any.whl.metadata (2.3 kB)\n",
            "Collecting langsmith<0.2.0,>=0.1.17 (from langchain)\n",
            "  Downloading langsmith-0.1.137-py3-none-any.whl.metadata (13 kB)\n",
            "Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.26.4)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.9.2)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.32.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (9.0.0)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.4.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (24.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.1.0)\n",
            "Requirement already satisfied: yarl<2.0,>=1.12.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.16.0)\n",
            "Collecting jsonpatch<2.0,>=1.33 (from langchain-core<0.4.0,>=0.3.12->langchain)\n",
            "  Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4.0,>=0.3.12->langchain) (24.1)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4.0,>=0.3.12->langchain) (4.12.2)\n",
            "Collecting httpx<1,>=0.23.0 (from langsmith<0.2.0,>=0.1.17->langchain)\n",
            "  Downloading httpx-0.27.2-py3-none-any.whl.metadata (7.1 kB)\n",
            "Collecting orjson<4.0.0,>=3.9.14 (from langsmith<0.2.0,>=0.1.17->langchain)\n",
            "  Downloading orjson-3.10.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (50 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.6/50.6 kB\u001b[0m \u001b[31m360.6 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting requests-toolbelt<2.0.0,>=1.0.0 (from langsmith<0.2.0,>=0.1.17->langchain)\n",
            "  Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.23.4 in /usr/local/lib/python3.10/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.23.4)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2024.8.30)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.1.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (3.7.1)\n",
            "Collecting httpcore==1.* (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain)\n",
            "  Downloading httpcore-1.0.6-py3-none-any.whl.metadata (21 kB)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.3.1)\n",
            "Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain)\n",
            "  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)\n",
            "Collecting jsonpointer>=1.9 (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.12->langchain)\n",
            "  Downloading jsonpointer-3.0.0-py2.py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.10/dist-packages (from yarl<2.0,>=1.12.0->aiohttp<4.0.0,>=3.8.3->langchain) (0.2.0)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.2.0,>=0.1.17->langchain) (1.2.2)\n",
            "Downloading langchain-0.3.4-py3-none-any.whl (1.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.0/1.0 MB\u001b[0m \u001b[31m14.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_core-0.3.12-py3-none-any.whl (407 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m407.7/407.7 kB\u001b[0m \u001b[31m18.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_text_splitters-0.3.0-py3-none-any.whl (25 kB)\n",
            "Downloading langsmith-0.1.137-py3-none-any.whl (296 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m296.9/296.9 kB\u001b[0m \u001b[31m14.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpx-0.27.2-py3-none-any.whl (76 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m76.4/76.4 kB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpcore-1.0.6-py3-none-any.whl (78 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m78.0/78.0 kB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)\n",
            "Downloading orjson-3.10.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (144 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m144.5/144.5 kB\u001b[0m \u001b[31m8.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.5/54.5 kB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)\n",
            "Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m3.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: orjson, jsonpointer, h11, requests-toolbelt, jsonpatch, httpcore, httpx, langsmith, langchain-core, langchain-text-splitters, langchain\n",
            "Successfully installed h11-0.14.0 httpcore-1.0.6 httpx-0.27.2 jsonpatch-1.33 jsonpointer-3.0.0 langchain-0.3.4 langchain-core-0.3.12 langchain-text-splitters-0.3.0 langsmith-0.1.137 orjson-3.10.10 requests-toolbelt-1.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install langchain"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain-groq"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "wt8WwtfLl8q3",
        "outputId": "0b5269d0-95a3-4a57-b9ca-6c9bd48c913d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain-groq\n",
            "  Downloading langchain_groq-0.2.0-py3-none-any.whl.metadata (2.9 kB)\n",
            "Collecting groq<1,>=0.4.1 (from langchain-groq)\n",
            "  Downloading groq-0.11.0-py3-none-any.whl.metadata (13 kB)\n",
            "Requirement already satisfied: langchain-core<0.4,>=0.3 in /usr/local/lib/python3.10/dist-packages (from langchain-groq) (0.3.12)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from groq<1,>=0.4.1->langchain-groq) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from groq<1,>=0.4.1->langchain-groq) (1.7.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from groq<1,>=0.4.1->langchain-groq) (0.27.2)\n",
            "Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from groq<1,>=0.4.1->langchain-groq) (2.9.2)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from groq<1,>=0.4.1->langchain-groq) (1.3.1)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from groq<1,>=0.4.1->langchain-groq) (4.12.2)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4,>=0.3->langchain-groq) (6.0.2)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4,>=0.3->langchain-groq) (1.33)\n",
            "Requirement already satisfied: langsmith<0.2.0,>=0.1.125 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4,>=0.3->langchain-groq) (0.1.136)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4,>=0.3->langchain-groq) (24.1)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.4,>=0.3->langchain-groq) (9.0.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->groq<1,>=0.4.1->langchain-groq) (3.10)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->groq<1,>=0.4.1->langchain-groq) (1.2.2)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->groq<1,>=0.4.1->langchain-groq) (2024.8.30)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->groq<1,>=0.4.1->langchain-groq) (1.0.6)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->groq<1,>=0.4.1->langchain-groq) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4,>=0.3->langchain-groq) (3.0.0)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.125->langchain-core<0.4,>=0.3->langchain-groq) (3.10.9)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.125->langchain-core<0.4,>=0.3->langchain-groq) (2.32.3)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.125->langchain-core<0.4,>=0.3->langchain-groq) (1.0.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->groq<1,>=0.4.1->langchain-groq) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.23.4 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->groq<1,>=0.4.1->langchain-groq) (2.23.4)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith<0.2.0,>=0.1.125->langchain-core<0.4,>=0.3->langchain-groq) (3.3.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langsmith<0.2.0,>=0.1.125->langchain-core<0.4,>=0.3->langchain-groq) (2.2.3)\n",
            "Downloading langchain_groq-0.2.0-py3-none-any.whl (14 kB)\n",
            "Downloading groq-0.11.0-py3-none-any.whl (106 kB)\n",
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/106.5 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m106.5/106.5 kB\u001b[0m \u001b[31m11.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: groq, langchain-groq\n",
            "Successfully installed groq-0.11.0 langchain-groq-0.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_groq import ChatGroq\n",
        "\n",
        "llm = ChatGroq(\n",
        "    model=\"llama-3.1-70b-versatile\",\n",
        "    temperature=0,\n",
        "    groq_api_key=\"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\"\n",
        ")\n",
        "\n",
        "response=llm.invoke(\"The first person to land on the moon was...\")\n",
        "print(response.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SM47xlV8mach",
        "outputId": "75531b6a-9347-42b7-cd8b-090cc311e458"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Neil Armstrong. He stepped onto the moon's surface on July 20, 1969, during the Apollo 11 mission.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install chromadb"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "MaTT52iUntNc",
        "outputId": "e3f47f55-c16f-4060-ef38-8289929d84e6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting chromadb\n",
            "  Downloading chromadb-0.5.15-py3-none-any.whl.metadata (6.8 kB)\n",
            "Requirement already satisfied: build>=1.0.3 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.2.2)\n",
            "Requirement already satisfied: pydantic>=1.9 in /usr/local/lib/python3.10/dist-packages (from chromadb) (2.9.2)\n",
            "Collecting chroma-hnswlib==0.7.6 (from chromadb)\n",
            "  Downloading chroma_hnswlib-0.7.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (252 bytes)\n",
            "Collecting fastapi>=0.95.2 (from chromadb)\n",
            "  Downloading fastapi-0.115.2-py3-none-any.whl.metadata (27 kB)\n",
            "Collecting uvicorn>=0.18.3 (from uvicorn[standard]>=0.18.3->chromadb)\n",
            "  Downloading uvicorn-0.32.0-py3-none-any.whl.metadata (6.6 kB)\n",
            "Requirement already satisfied: numpy>=1.22.5 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.26.4)\n",
            "Collecting posthog>=2.4.0 (from chromadb)\n",
            "  Downloading posthog-3.7.0-py2.py3-none-any.whl.metadata (2.0 kB)\n",
            "Requirement already satisfied: typing-extensions>=4.5.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (4.12.2)\n",
            "Collecting onnxruntime>=1.14.1 (from chromadb)\n",
            "  Downloading onnxruntime-1.19.2-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (4.5 kB)\n",
            "Collecting opentelemetry-api>=1.2.0 (from chromadb)\n",
            "  Downloading opentelemetry_api-1.27.0-py3-none-any.whl.metadata (1.4 kB)\n",
            "Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb)\n",
            "  Downloading opentelemetry_exporter_otlp_proto_grpc-1.27.0-py3-none-any.whl.metadata (2.3 kB)\n",
            "Collecting opentelemetry-instrumentation-fastapi>=0.41b0 (from chromadb)\n",
            "  Downloading opentelemetry_instrumentation_fastapi-0.48b0-py3-none-any.whl.metadata (2.1 kB)\n",
            "Collecting opentelemetry-sdk>=1.2.0 (from chromadb)\n",
            "  Downloading opentelemetry_sdk-1.27.0-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: tokenizers>=0.13.2 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.19.1)\n",
            "Collecting pypika>=0.48.9 (from chromadb)\n",
            "  Downloading PyPika-0.48.9.tar.gz (67 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.3/67.3 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (4.66.5)\n",
            "Collecting overrides>=7.3.1 (from chromadb)\n",
            "  Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.10/dist-packages (from chromadb) (6.4.5)\n",
            "Requirement already satisfied: grpcio>=1.58.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.64.1)\n",
            "Collecting bcrypt>=4.0.1 (from chromadb)\n",
            "  Downloading bcrypt-4.2.0-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (9.6 kB)\n",
            "Requirement already satisfied: typer>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.12.5)\n",
            "Collecting kubernetes>=28.1.0 (from chromadb)\n",
            "  Downloading kubernetes-31.0.0-py2.py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: tenacity>=8.2.3 in /usr/local/lib/python3.10/dist-packages (from chromadb) (9.0.0)\n",
            "Requirement already satisfied: PyYAML>=6.0.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (6.0.2)\n",
            "Collecting mmh3>=4.0.1 (from chromadb)\n",
            "  Downloading mmh3-5.0.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (14 kB)\n",
            "Requirement already satisfied: orjson>=3.9.12 in /usr/local/lib/python3.10/dist-packages (from chromadb) (3.10.9)\n",
            "Requirement already satisfied: httpx>=0.27.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.27.2)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (13.8.1)\n",
            "Requirement already satisfied: packaging>=19.1 in /usr/local/lib/python3.10/dist-packages (from build>=1.0.3->chromadb) (24.1)\n",
            "Requirement already satisfied: pyproject_hooks in /usr/local/lib/python3.10/dist-packages (from build>=1.0.3->chromadb) (1.1.0)\n",
            "Requirement already satisfied: tomli>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from build>=1.0.3->chromadb) (2.0.1)\n",
            "Collecting starlette<0.41.0,>=0.37.2 (from fastapi>=0.95.2->chromadb)\n",
            "  Downloading starlette-0.40.0-py3-none-any.whl.metadata (6.0 kB)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->chromadb) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->chromadb) (2024.8.30)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->chromadb) (1.0.6)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->chromadb) (3.10)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->chromadb) (1.3.1)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx>=0.27.0->chromadb) (0.14.0)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (1.16.0)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.8.2)\n",
            "Requirement already satisfied: google-auth>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.27.0)\n",
            "Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (1.8.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.32.3)\n",
            "Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (1.3.1)\n",
            "Requirement already satisfied: oauthlib>=3.2.2 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (3.2.2)\n",
            "Requirement already satisfied: urllib3>=1.24.2 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.2.3)\n",
            "Collecting durationpy>=0.7 (from kubernetes>=28.1.0->chromadb)\n",
            "  Downloading durationpy-0.9-py3-none-any.whl.metadata (338 bytes)\n",
            "Collecting coloredlogs (from onnxruntime>=1.14.1->chromadb)\n",
            "  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)\n",
            "Requirement already satisfied: flatbuffers in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (24.3.25)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (3.20.3)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (1.13.3)\n",
            "Collecting deprecated>=1.2.6 (from opentelemetry-api>=1.2.0->chromadb)\n",
            "  Downloading Deprecated-1.2.14-py2.py3-none-any.whl.metadata (5.4 kB)\n",
            "Collecting importlib-metadata<=8.4.0,>=6.0 (from opentelemetry-api>=1.2.0->chromadb)\n",
            "  Downloading importlib_metadata-8.4.0-py3-none-any.whl.metadata (4.7 kB)\n",
            "Requirement already satisfied: googleapis-common-protos~=1.52 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.65.0)\n",
            "Collecting opentelemetry-exporter-otlp-proto-common==1.27.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb)\n",
            "  Downloading opentelemetry_exporter_otlp_proto_common-1.27.0-py3-none-any.whl.metadata (1.8 kB)\n",
            "Collecting opentelemetry-proto==1.27.0 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb)\n",
            "  Downloading opentelemetry_proto-1.27.0-py3-none-any.whl.metadata (2.3 kB)\n",
            "Collecting opentelemetry-instrumentation-asgi==0.48b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)\n",
            "  Downloading opentelemetry_instrumentation_asgi-0.48b0-py3-none-any.whl.metadata (2.0 kB)\n",
            "Collecting opentelemetry-instrumentation==0.48b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)\n",
            "  Downloading opentelemetry_instrumentation-0.48b0-py3-none-any.whl.metadata (6.1 kB)\n",
            "Collecting opentelemetry-semantic-conventions==0.48b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)\n",
            "  Downloading opentelemetry_semantic_conventions-0.48b0-py3-none-any.whl.metadata (2.4 kB)\n",
            "Collecting opentelemetry-util-http==0.48b0 (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)\n",
            "  Downloading opentelemetry_util_http-0.48b0-py3-none-any.whl.metadata (2.5 kB)\n",
            "Requirement already satisfied: setuptools>=16.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation==0.48b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (71.0.4)\n",
            "Requirement already satisfied: wrapt<2.0.0,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation==0.48b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (1.16.0)\n",
            "Collecting asgiref~=3.0 (from opentelemetry-instrumentation-asgi==0.48b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb)\n",
            "  Downloading asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)\n",
            "Collecting monotonic>=1.5 (from posthog>=2.4.0->chromadb)\n",
            "  Downloading monotonic-1.6-py2.py3-none-any.whl.metadata (1.5 kB)\n",
            "Collecting backoff>=1.10.0 (from posthog>=2.4.0->chromadb)\n",
            "  Downloading backoff-2.2.1-py3-none-any.whl.metadata (14 kB)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=1.9->chromadb) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.23.4 in /usr/local/lib/python3.10/dist-packages (from pydantic>=1.9->chromadb) (2.23.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->chromadb) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->chromadb) (2.18.0)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.16.4 in /usr/local/lib/python3.10/dist-packages (from tokenizers>=0.13.2->chromadb) (0.24.7)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from typer>=0.9.0->chromadb) (8.1.7)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer>=0.9.0->chromadb) (1.5.4)\n",
            "Collecting httptools>=0.5.0 (from uvicorn[standard]>=0.18.3->chromadb)\n",
            "  Downloading httptools-0.6.4-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.6 kB)\n",
            "Collecting python-dotenv>=0.13 (from uvicorn[standard]>=0.18.3->chromadb)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0 (from uvicorn[standard]>=0.18.3->chromadb)\n",
            "  Downloading uvloop-0.21.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)\n",
            "Collecting watchfiles>=0.13 (from uvicorn[standard]>=0.18.3->chromadb)\n",
            "  Downloading watchfiles-0.24.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)\n",
            "Collecting websockets>=10.4 (from uvicorn[standard]>=0.18.3->chromadb)\n",
            "  Downloading websockets-13.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (5.5.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.4.1)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (4.9)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb) (3.16.1)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb) (2024.6.1)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata<=8.4.0,>=6.0->opentelemetry-api>=1.2.0->chromadb) (3.20.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb) (0.1.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->kubernetes>=28.1.0->chromadb) (3.3.2)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio->httpx>=0.27.0->chromadb) (1.2.2)\n",
            "Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime>=1.14.1->chromadb)\n",
            "  Downloading humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->onnxruntime>=1.14.1->chromadb) (1.3.0)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.6.1)\n",
            "Downloading chromadb-0.5.15-py3-none-any.whl (607 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m607.0/607.0 kB\u001b[0m \u001b[31m33.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading chroma_hnswlib-0.7.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.4/2.4 MB\u001b[0m \u001b[31m64.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading bcrypt-4.2.0-cp39-abi3-manylinux_2_28_x86_64.whl (273 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m273.8/273.8 kB\u001b[0m \u001b[31m23.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading fastapi-0.115.2-py3-none-any.whl (94 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m94.7/94.7 kB\u001b[0m \u001b[31m9.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading kubernetes-31.0.0-py2.py3-none-any.whl (1.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.9/1.9 MB\u001b[0m \u001b[31m65.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading mmh3-5.0.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (93 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m93.2/93.2 kB\u001b[0m \u001b[31m8.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading onnxruntime-1.19.2-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (13.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.2/13.2 MB\u001b[0m \u001b[31m80.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_api-1.27.0-py3-none-any.whl (63 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m64.0/64.0 kB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_exporter_otlp_proto_grpc-1.27.0-py3-none-any.whl (18 kB)\n",
            "Downloading opentelemetry_exporter_otlp_proto_common-1.27.0-py3-none-any.whl (17 kB)\n",
            "Downloading opentelemetry_proto-1.27.0-py3-none-any.whl (52 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m52.5/52.5 kB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_instrumentation_fastapi-0.48b0-py3-none-any.whl (11 kB)\n",
            "Downloading opentelemetry_instrumentation-0.48b0-py3-none-any.whl (29 kB)\n",
            "Downloading opentelemetry_instrumentation_asgi-0.48b0-py3-none-any.whl (15 kB)\n",
            "Downloading opentelemetry_semantic_conventions-0.48b0-py3-none-any.whl (149 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m149.7/149.7 kB\u001b[0m \u001b[31m11.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading opentelemetry_util_http-0.48b0-py3-none-any.whl (6.9 kB)\n",
            "Downloading opentelemetry_sdk-1.27.0-py3-none-any.whl (110 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m110.5/110.5 kB\u001b[0m \u001b[31m10.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading overrides-7.7.0-py3-none-any.whl (17 kB)\n",
            "Downloading posthog-3.7.0-py2.py3-none-any.whl (54 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.4/54.4 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading uvicorn-0.32.0-py3-none-any.whl (63 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m63.7/63.7 kB\u001b[0m \u001b[31m6.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading backoff-2.2.1-py3-none-any.whl (15 kB)\n",
            "Downloading Deprecated-1.2.14-py2.py3-none-any.whl (9.6 kB)\n",
            "Downloading durationpy-0.9-py3-none-any.whl (3.5 kB)\n",
            "Downloading httptools-0.6.4-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (442 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m442.1/442.1 kB\u001b[0m \u001b[31m32.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading importlib_metadata-8.4.0-py3-none-any.whl (26 kB)\n",
            "Downloading monotonic-1.6-py2.py3-none-any.whl (8.2 kB)\n",
            "Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading starlette-0.40.0-py3-none-any.whl (73 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.3/73.3 kB\u001b[0m \u001b[31m6.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading uvloop-0.21.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.8/3.8 MB\u001b[0m \u001b[31m60.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchfiles-0.24.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (425 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m425.7/425.7 kB\u001b[0m \u001b[31m29.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading websockets-13.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (164 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.1/164.1 kB\u001b[0m \u001b[31m16.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m46.0/46.0 kB\u001b[0m \u001b[31m4.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading asgiref-3.8.1-py3-none-any.whl (23 kB)\n",
            "Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m86.8/86.8 kB\u001b[0m \u001b[31m8.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hBuilding wheels for collected packages: pypika\n",
            "  Building wheel for pypika (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pypika: filename=PyPika-0.48.9-py2.py3-none-any.whl size=53725 sha256=b5ab835e8b3539080cf8025ec0dfeaf62fcb46f37be279c0de2f95d317793dc6\n",
            "  Stored in directory: /root/.cache/pip/wheels/e1/26/51/d0bffb3d2fd82256676d7ad3003faea3bd6dddc9577af665f4\n",
            "Successfully built pypika\n",
            "Installing collected packages: pypika, monotonic, durationpy, websockets, uvloop, uvicorn, python-dotenv, overrides, opentelemetry-util-http, opentelemetry-proto, mmh3, importlib-metadata, humanfriendly, httptools, deprecated, chroma-hnswlib, bcrypt, backoff, asgiref, watchfiles, starlette, posthog, opentelemetry-exporter-otlp-proto-common, opentelemetry-api, coloredlogs, opentelemetry-semantic-conventions, opentelemetry-instrumentation, onnxruntime, kubernetes, fastapi, opentelemetry-sdk, opentelemetry-instrumentation-asgi, opentelemetry-instrumentation-fastapi, opentelemetry-exporter-otlp-proto-grpc, chromadb\n",
            "  Attempting uninstall: importlib-metadata\n",
            "    Found existing installation: importlib_metadata 8.5.0\n",
            "    Uninstalling importlib_metadata-8.5.0:\n",
            "      Successfully uninstalled importlib_metadata-8.5.0\n",
            "Successfully installed asgiref-3.8.1 backoff-2.2.1 bcrypt-4.2.0 chroma-hnswlib-0.7.6 chromadb-0.5.15 coloredlogs-15.0.1 deprecated-1.2.14 durationpy-0.9 fastapi-0.115.2 httptools-0.6.4 humanfriendly-10.0 importlib-metadata-8.4.0 kubernetes-31.0.0 mmh3-5.0.1 monotonic-1.6 onnxruntime-1.19.2 opentelemetry-api-1.27.0 opentelemetry-exporter-otlp-proto-common-1.27.0 opentelemetry-exporter-otlp-proto-grpc-1.27.0 opentelemetry-instrumentation-0.48b0 opentelemetry-instrumentation-asgi-0.48b0 opentelemetry-instrumentation-fastapi-0.48b0 opentelemetry-proto-1.27.0 opentelemetry-sdk-1.27.0 opentelemetry-semantic-conventions-0.48b0 opentelemetry-util-http-0.48b0 overrides-7.7.0 posthog-3.7.0 pypika-0.48.9 python-dotenv-1.0.1 starlette-0.40.0 uvicorn-0.32.0 uvloop-0.21.0 watchfiles-0.24.0 websockets-13.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import chromadb\n",
        "client=chromadb.Client()\n",
        "collection=client.create_collection(\"my_collection\")"
      ],
      "metadata": {
        "id": "P_XF5KG7qFAa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "collection.add(\n",
        "    documents=[\n",
        "        'This document is about New York',\n",
        "        'This document is about California',\n",
        "        'This document is about Washington'\n",
        "    ],\n",
        "    ids=['id1','id2','id3']\n",
        ")\n",
        "all_docs=collection.get()\n",
        "all_docs"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SAq_Mg7pqxiR",
        "outputId": "4315031c-6f98-4775-f44d-10a60daf403e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/root/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx.tar.gz: 100%|██████████| 79.3M/79.3M [00:01<00:00, 56.3MiB/s]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'ids': ['id1', 'id2', 'id3'],\n",
              " 'embeddings': None,\n",
              " 'documents': ['This document is about New York',\n",
              "  'This document is about California',\n",
              "  'This document is about Washington'],\n",
              " 'uris': None,\n",
              " 'data': None,\n",
              " 'metadatas': [None, None, None],\n",
              " 'included': [<IncludeEnum.documents: 'documents'>,\n",
              "  <IncludeEnum.metadatas: 'metadatas'>]}"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "results=collection.query(\n",
        "    query_texts=['Query is about Tech Companies'],\n",
        "n_results=2\n",
        ")\n",
        "results"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rUnFvUYXrYFS",
        "outputId": "e13684ae-a415-4014-ab93-7e561f7fea09"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'ids': [['id2', 'id1']],\n",
              " 'embeddings': None,\n",
              " 'documents': [['This document is about California',\n",
              "   'This document is about New York']],\n",
              " 'uris': None,\n",
              " 'data': None,\n",
              " 'metadatas': [[None, None]],\n",
              " 'distances': [[1.7189438343048096, 1.864328384399414]],\n",
              " 'included': [<IncludeEnum.distances: 'distances'>,\n",
              "  <IncludeEnum.documents: 'documents'>,\n",
              "  <IncludeEnum.metadatas: 'metadatas'>]}"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -qU langchain_community beautifulsoup4"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zbU6itKFunH1",
        "outputId": "bd7bd28d-c427-4f8b-8250-57f1b44dd483"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/2.4 MB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.4/2.4 MB\u001b[0m \u001b[31m73.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/49.5 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.5/49.5 kB\u001b[0m \u001b[31m1.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.document_loaders import WebBaseLoader\n",
        "loader = WebBaseLoader('https://jobs.nike.com/job/R-38694?from=job%20search%20funnel')\n",
        "page_data=loader.load().pop().page_content\n",
        "page_data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 229
        },
        "id": "OmZDd1o9sXLk",
        "outputId": "029045d0-b37a-4d8d-d0e2-3dd5f00c401b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:langchain_community.utils.user_agent:USER_AGENT environment variable not set, consider setting it to identify your requests.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"Apply for Entry ML Engineer (Remote Work Option)\\n\\nSearch JobsSkip navigationSearch JobsNIKE, INC. JOBSContract JobsJoin The Talent CommunityLife @ NikeOverviewBenefitsBrandsOverviewJordanConverseTeamsOverviewAdministrative SupportAdvanced InnovationAir Manufacturing InnovationAviationCommunicationsCustomer ServiceDesignDigitalFacilitiesFinance & AccountingGovernment & Public AffairsHuman ResourcesInsights & AnalyticsLegalManufacturing & EngineeringMarketingMerchandisingPlanningPrivacyProcurementProduct Creation, Development & ManagementRetail CorporateRetail StoresSalesSocial & Community ImpactSports MarketingStrategic PlanningSupply Chain, Distribution & LogisticsSustainabilityTechnologyLocationsOverviewNike WHQNike New York HQEHQ: Hilversum, The NetherlandsELC: Laakdal, BelgiumGreater China HQDiversity, Equity & InclusionOverviewMilitary InclusionDisability InclusionIndigenous InclusionInternshipsData & AnalyticsEntry ML Engineer (Remote Work Option)Beaverton, OregonBecome a Part of the NIKE, Inc. Team\\nNIKE, Inc. does more than outfit the world’s best athletes. It is a place to explore potential, obliterate boundaries and push out the edges of what can be. The company looks for people who can grow, think, dream and create. Its culture thrives by embracing diversity and rewarding imagination. The brand seeks achievers, leaders and visionaries. At NIKE, Inc. it’s about each person bringing skills and passion to a challenging and constantly evolving game.Open to remote work except in South Dakota, Vermont and West Virginia.The annual base salary for this position ranges from $69,100.00 in our lowest geographic market to $154,900.00 in our highest geographic market. Actual salary will vary based on a candidate's location, qualifications, skills and experience.Information about benefits can be found here.\\xa0Who are we looking forWe are actively seeking to hire a Entry Level Machine Learning Engineers to join our AI/ML team. As a Machine Learning Engineer within the AI/ML team, you will be developing advanced analytics systems that directly impact our business. You will work on a cross-disciplinary team (data/API/infra/infosec/ML) to enable data-driven decision making across multiple organizations.Working at the intersection of machine learning and software engineering (i.e., MLOps), you’ll create high-quality solutions that power Nike. You will work with others who are energized by the challenge of building things from the ground up, thinking out of the box, and applying the latest technologies in statistical, unsupervised, supervised, and machine learning models at global scale.Our teams enjoy a collaborative and academic environment that promotes developing new skills, mentorship, and a drive to deliver knowledge and software back to analytics and engineering communities, within and Nike and without. This culture is cultivated by intellectual curiosity, fun, openness, and diversity.Sound like you?Who will you work withAI/ML is one of the key groups within Data and Analytics. We’re chartered to scale machine learning and AI at Nike. For areas of the business early in their analytics journey, we embed cross-disciplinary teams of data scientists and engineers to unlock new capabilities and answer unsolved (or unasked!) questions. In mature areas with pre-existing data science teams, we help scale machine learning by attaching engineering squads to grow their capacity to deliver for the business. In addition, we collaborate closely with platform and architecture partners to develop capabilities that simplify machine learning at scale within Nike (e.g. model management, A/B testing, feature stores).Essential Job Functions:Serve as an integral member of a multi-functional engineering teams that delivers solutions unlocking machine learning for Nike. You will analyze and profile data to uncover insights in support of scalable solutions, clean, prepare and verify the integrity of data for analysis and model creation. You’ll also track model accuracy, performance, relevance, and reliability. You will apply a variety of machine learning and collaborative filtering methods to data sets. You will aid in building APIs and software libraries that support adoption of models in productionLeverage your prior experience, knowledge of industry trends, and personal creativity to develop new and innovative solutions which delight our customers in their mission to serve Athletes*.Stay ahead of with industry trends and recommend relevant technologies & products in the areas of Analytics, Machine Learning, Artificial Intelligence, and Data Science tools and other emerging technologies. Given the rapid pace of change in technology and machine learning today, always be pushing the boundary of what’s possible and be on the offense always.Embrace and embody Nike’s core values (Maxims) in your work and interactions with peers and stakeholders. Communicate effectively, building trust and strong relationships across the company, do the right thing.What you bring to NikeBachelor’s degree or a combination of relevant education, training, and experiencein the field of ML Engineering or Software EngineeringOne year of experience preferredUnderstanding of Machine Learning, its applications, and the lifecycle of an ML application in production; including an ability to articulate the role of MLOps in model development from experimentation to production and measurementAn ability to meaningfully communicate, written, orally, and visually technical topics with peers and articulate the benefits and tradeoffs of various solutionsExperience working in and/or collaborating with a partial or fully distributed teamStrong experiential understanding of data structures, algorithms, and data solutionsExperience in applying Python (or another language commonly used in the field of ML, such as Scala, Julia, C++) and SQL to ML and/or software and data engineering tasksFamiliarity with ETL, ML, or analytics technologies such as Scikit-learn, Dask, TensorFlow, Kubeflow, Spark, EMR, or similar platforms and frameworksAwareness of data science platforms (like Databricks or SageMaker), distributed engines (like Spark and AWS cloud), and CI/CD pipelines and containerization are preferredFluency in the application of open-source technologies and the potential of standardized platforms in the area of Data Science, AI, & ML.Nice to have: an interest in the potential of Generative AI to accelerate common development and data science tasks, or the deployment of Generative AI solutions in the enterpriseNIKE, Inc. is a growth company that looks for team members to grow with it. Nike offers a generous total rewards package, casual work environment, a diverse and inclusive culture, and an electric atmosphere for professional development. No matter the location, or the role, every Nike employee shares one galvanizing mission: To bring inspiration and innovation to every athlete* in the world.NIKE, Inc. is committed to employing a diverse workforce. Qualified applicants will receive consideration without regard to race, color, religion, sex, national origin, age, sexual orientation, gender identity, gender expression, veteran status, or disability.How We HireAt NIKE, Inc. we promise to provide a premium, inclusive, compelling and authentic candidate experience. Delivering on this promise means we allow you to be at your best — and to do that, you need to understand how the hiring process works. Transparency is key.\\r\\n\\r\\n* This overview explains our hiring process for corporate roles. Note there may be different hiring steps involved for non-corporate roles.Start nowBenefitsWhether it’s transportation or financial health, we continually invest in our employees to help them achieve greatness — inside and outside of work. All who work here should be able to realize their full potential.Employee Assistance ProgramEmployee Stock Purchase Plan (ESPP)HolidaysMedical PlanPaid Time Off (PTO)Product DiscountsSabbaticalsLearn moreGIFT CARDSPROMOTIONSFIND A STORESIGN UP FOR EMAILBECOME A MEMBERNIKE JOURNALSEND US FEEDBACKGET HELPGET HELPOrder StatusShipping and DeliveryReturnsPayment OptionsGift Cards BalanceContact UsABOUT NIKEABOUT NIKENewsCareersInvestorsPurposeSustainabilityUnited States© 2024 Nike, Inc. All Rights ReservedGuidesNike AdaptNike Air MaxNike FlyleatherNike ReactSpace HippieNike AirNike FlyEaseNike Free Nike VaporflyNike Air Force 1 Nike FlyknitNike JoyrideNike ZoomXTerms of SaleTerms of UseNike Privacy PolicyYour Privacy ChoicesCA Supply Chain Act\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.prompts import PromptTemplate\n",
        "prompt_extract=PromptTemplate.from_template(\n",
        "    \"\"\"\n",
        "    ### SCRAPED TEXT FROM WEBSITE:\n",
        "    {page_data}\n",
        "    ### INSTRUCTION:\n",
        "    The scraped text is from the careers page of a website.\n",
        "    Your job is to extract the job postings and return them in a JSON format containing\n",
        "    following keys: 'role','experience','skills',and 'description'.\n",
        "    Only return valid JSON.\n",
        "    ### VALID JSON (NO PREAMBLE)\n",
        "    \"\"\"\n",
        ")\n",
        "chain_extract=prompt_extract|llm\n",
        "res=chain_extract.invoke({'page_data':page_data})\n",
        "print(res.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oKD9aP3JvC1m",
        "outputId": "9a2526d4-a1ca-4b06-fd76-bce1fcb5a100"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "```json\n",
            "{\n",
            "  \"role\": \"Entry ML Engineer (Remote Work Option)\",\n",
            "  \"experience\": \"One year of experience preferred\",\n",
            "  \"skills\": [\n",
            "    \"Machine Learning\",\n",
            "    \"Software Engineering\",\n",
            "    \"Python\",\n",
            "    \"SQL\",\n",
            "    \"ETL\",\n",
            "    \"Scikit-learn\",\n",
            "    \"Dask\",\n",
            "    \"TensorFlow\",\n",
            "    \"Kubeflow\",\n",
            "    \"Spark\",\n",
            "    \"EMR\",\n",
            "    \"Databricks\",\n",
            "    \"SageMaker\",\n",
            "    \"CI/CD pipelines\",\n",
            "    \"Containerization\",\n",
            "    \"Open-source technologies\",\n",
            "    \"Data Science platforms\",\n",
            "    \"Distributed engines\",\n",
            "    \"Generative AI\"\n",
            "  ],\n",
            "  \"description\": \"We are actively seeking to hire a Entry Level Machine Learning Engineers to join our AI/ML team. As a Machine Learning Engineer within the AI/ML team, you will be developing advanced analytics systems that directly impact our business. You will work on a cross-disciplinary team (data/API/infra/infosec/ML) to enable data-driven decision making across multiple organizations.\"\n",
            "}\n",
            "```\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.output_parsers import JsonOutputParser\n",
        "json_parser=JsonOutputParser()\n",
        "json_res=json_parser.parse(res.content)\n",
        "json_res"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Wfx6U9Yzuly",
        "outputId": "ee9ede5d-d2c1-4363-cadb-7b4f084a63da"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'role': 'Entry ML Engineer (Remote Work Option)',\n",
              " 'experience': 'One year of experience preferred',\n",
              " 'skills': ['Machine Learning',\n",
              "  'Software Engineering',\n",
              "  'Python',\n",
              "  'SQL',\n",
              "  'ETL',\n",
              "  'Scikit-learn',\n",
              "  'Dask',\n",
              "  'TensorFlow',\n",
              "  'Kubeflow',\n",
              "  'Spark',\n",
              "  'EMR',\n",
              "  'Databricks',\n",
              "  'SageMaker',\n",
              "  'CI/CD pipelines',\n",
              "  'Containerization',\n",
              "  'Open-source technologies',\n",
              "  'Data Science platforms',\n",
              "  'Distributed engines',\n",
              "  'Generative AI'],\n",
              " 'description': 'We are actively seeking to hire a Entry Level Machine Learning Engineers to join our AI/ML team. As a Machine Learning Engineer within the AI/ML team, you will be developing advanced analytics systems that directly impact our business. You will work on a cross-disciplinary team (data/API/infra/infosec/ML) to enable data-driven decision making across multiple organizations.'}"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(json_res)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YzAKsWk423Gi",
        "outputId": "9085947c-7a59-4a10-9309-c4e1449e62e3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df=pd.read_csv('/content/drive/MyDrive/my_portfolio.csv')\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "J3ICQao325oo",
        "outputId": "6037ee1f-3691-4989-e6df-9a09567baa63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                           Techstack                                  Links\n",
              "0            React, Node.js, MongoDB    https://example.com/react-portfolio\n",
              "1           Angular,.NET, SQL Server  https://example.com/angular-portfolio\n",
              "2  Vue.js, Ruby on Rails, PostgreSQL      https://example.com/vue-portfolio\n",
              "3              Python, Django, MySQL   https://example.com/python-portfolio\n",
              "4          Java, Spring Boot, Oracle     https://example.com/java-portfolio"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-72800d49-da38-41ae-8ac8-f598c4fe27fe\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Techstack</th>\n",
              "      <th>Links</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>React, Node.js, MongoDB</td>\n",
              "      <td>https://example.com/react-portfolio</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Angular,.NET, SQL Server</td>\n",
              "      <td>https://example.com/angular-portfolio</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Vue.js, Ruby on Rails, PostgreSQL</td>\n",
              "      <td>https://example.com/vue-portfolio</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Python, Django, MySQL</td>\n",
              "      <td>https://example.com/python-portfolio</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Java, Spring Boot, Oracle</td>\n",
              "      <td>https://example.com/java-portfolio</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-72800d49-da38-41ae-8ac8-f598c4fe27fe')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-72800d49-da38-41ae-8ac8-f598c4fe27fe button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-72800d49-da38-41ae-8ac8-f598c4fe27fe');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-c4c913ca-eae7-4838-a994-8dac66ac2adc\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c4c913ca-eae7-4838-a994-8dac66ac2adc')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-c4c913ca-eae7-4838-a994-8dac66ac2adc button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 20,\n  \"fields\": [\n    {\n      \"column\": \"Techstack\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 20,\n        \"samples\": [\n          \"React, Node.js, MongoDB\",\n          \"Full-stack, JavaScript, Express.js\",\n          \"Backend, Kotlin, Spring Boot\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Links\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 20,\n        \"samples\": [\n          \"https://example.com/react-portfolio\",\n          \"https://example.com/full-stack-js-portfolio\",\n          \"https://example.com/kotlin-backend-portfolio\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import uuid\n",
        "client = chromadb.PersistentClient('vectorstore')\n",
        "collection = client.get_or_create_collection(name='portfolio')\n",
        "\n",
        "if not collection.count():\n",
        "  for _,row in df.iterrows():\n",
        "    collection.add(documents=row[\"Techstack\"],\n",
        "    metadatas={'links':row[\"Links\"]},\n",
        "    ids=[str(uuid.uuid4())])\n"
      ],
      "metadata": {
        "id": "dKgqMHLDE1Lk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "links=collection.query(query_texts=[\"skills\"],n_results=2).get('metadatas')\n",
        "links"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tmwBGBKhGaJx",
        "outputId": "3d7c442b-6309-4d44-a5e3-e8fd0ac23d02"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[{'links': 'https://example.com/ml-python-portfolio'},\n",
              "  {'links': 'https://example.com/python-portfolio'}]]"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "job=json_res\n",
        "job['skills']"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NsrI2e3gItcD",
        "outputId": "64575ded-a48a-4811-86a5-87ee0043efd8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Machine Learning',\n",
              " 'Software Engineering',\n",
              " 'Python',\n",
              " 'SQL',\n",
              " 'ETL',\n",
              " 'Scikit-learn',\n",
              " 'Dask',\n",
              " 'TensorFlow',\n",
              " 'Kubeflow',\n",
              " 'Spark',\n",
              " 'EMR',\n",
              " 'Databricks',\n",
              " 'SageMaker',\n",
              " 'CI/CD pipelines',\n",
              " 'Containerization',\n",
              " 'Open-source technologies',\n",
              " 'Data Science platforms',\n",
              " 'Distributed engines',\n",
              " 'Generative AI']"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "prompt_email = PromptTemplate.from_template(\n",
        "        \"\"\"\n",
        "        ### JOB DESCRIPTION:\n",
        "        {job_description}\n",
        "\n",
        "        ### INSTRUCTION:\n",
        "        You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating\n",
        "        the seamless integration of business processes through automated tools.\n",
        "        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,\n",
        "        process optimization, cost reduction, and heightened overall efficiency.\n",
        "        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of StarCom\n",
        "        in fulfilling their needs.\n",
        "        Also add the most relevant ones from the following links to showcase StarCom's portfolio: {link_list}\n",
        "        Remember you are Astika, BDE at StarCom.\n",
        "        Do not provide a preamble.\n",
        "        ### EMAIL (NO PREAMBLE):\n",
        "\n",
        "        \"\"\"\n",
        "        )\n",
        "chain_email = prompt_email | llm\n",
        "res=chain_email.invoke({'job_description':str(job),'link_list':links})\n",
        "print(res.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8_yURjmVJRW5",
        "outputId": "3f0fdaad-42d7-48a6-803d-85d02d28e57c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Subject: Expert Machine Learning Solutions for Your Business Needs\n",
            "\n",
            "Dear Hiring Manager,\n",
            "\n",
            "I came across the job posting for an Entry ML Engineer (Remote Work Option) and was impressed by the cutting-edge technologies your team is working with. As a Business Development Executive at AtliQ, I'd like to introduce you to our AI & Software Consulting company, dedicated to empowering businesses like yours with tailored solutions.\n",
            "\n",
            "Our team of experts has extensive experience in developing advanced analytics systems, leveraging Machine Learning, Software Engineering, and Data Science platforms. We've successfully delivered projects utilizing Scikit-learn, TensorFlow, Kubeflow, Spark, and other distributed engines. Our proficiency in CI/CD pipelines, Containerization, and Open-source technologies ensures seamless integration and scalability.\n",
            "\n",
            "I'd like to highlight a few relevant projects from our portfolio that demonstrate our capabilities:\n",
            "\n",
            "* [https://example.com/ml-python-portfolio](https://example.com/ml-python-portfolio) - A showcase of our expertise in Machine Learning and Python development.\n",
            "* [https://example.com/python-portfolio](https://example.com/python-portfolio) - A collection of our projects utilizing Python for various business applications.\n",
            "\n",
            "At AtliQ, we understand the importance of data-driven decision making and have helped numerous enterprises optimize their processes, reduce costs, and enhance overall efficiency. Our team is well-equipped to support your AI/ML team in developing advanced analytics systems that directly impact your business.\n",
            "\n",
            "If you're looking for a reliable partner to augment your team's capabilities or need assistance with specific projects, I'd be happy to schedule a call to discuss further. Please let me know if you'd like to explore how AtliQ can support your business needs.\n",
            "\n",
            "Best regards,\n",
            "\n",
            "Mohan\n",
            "Business Development Executive\n",
            "AtliQ\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "VdVY81rQKUla",
        "outputId": "653d75b2-f741-4999-87a5-d352a2580e4f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.39.0-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (10.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.8.1)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<6,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-5.0.3-py3-none-manylinux2014_x86_64.whl.metadata (41 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.9/41.9 kB\u001b[0m \u001b[31m3.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.39.0-py2.py3-none-any.whl (8.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.7/8.7 MB\u001b[0m \u001b[31m97.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m17.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m95.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-5.0.3-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.3/79.3 kB\u001b[0m \u001b[31m7.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: watchdog, smmap, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed gitdb-4.0.11 gitpython-3.1.43 pydeck-0.9.1 smmap-5.0.1 streamlit-1.39.0 watchdog-5.0.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "\n",
        "st.title(\"Cold Email Generation\")\n",
        "url_input = st.text_input(\"Enter the URL\",value='https://jobs.nike.com/job/R-38694?from=job%20search%20funnel')\n",
        "submit_button = st.button(\"Submit\")\n",
        "\n",
        "if submit_button:\n",
        "  st.code(\"Hello Hiring Manager, I'm from ABC\",language='markdown')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QLKFKqL6NXTe",
        "outputId": "c4e61fa3-1940-436b-965b-f25656b1ed5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AW621YzkOld8",
        "outputId": "53148640-5872-427e-c5e7-2bc979fb4eb1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.2:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.85.196.188:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "vL6jfrbpOtUF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}