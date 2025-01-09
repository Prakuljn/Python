{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqfhFc2Zdfpd8I7gkfVOXQ",
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
        "<a href=\"https://colab.research.google.com/github/Prakuljn/Python-Assignment/blob/main/09%20january%20assignment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4nyAqpZOQKEZ",
        "outputId": "6ee55ee5-08a3-4aa4-ad34-d2c56c444ad7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number to print12\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "11\n"
          ]
        }
      ],
      "source": [
        "# Question 1\n",
        "\n",
        "n = int(input(\"enter number to print\"))\n",
        "i=1\n",
        "while i<=n:\n",
        "    print(i)\n",
        "    i+=1"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 2\n",
        "\n",
        "n = int(input(\"enter number to print\"))\n",
        "i=n\n",
        "while n>0:\n",
        "    print(n)\n",
        "    n-=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZOxRJxF-QnNB",
        "outputId": "952c2837-55e3-490e-f2fd-73015c96c10e"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number to print12\n",
            "12\n",
            "11\n",
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 3\n",
        "i=97\n",
        "while chr(i)<chr(122):\n",
        "    print(chr(i))\n",
        "    i+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3r940I0XRcRS",
        "outputId": "3635e2c3-3910-4be6-a468-452982bf8253"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "a\n",
            "b\n",
            "c\n",
            "d\n",
            "e\n",
            "f\n",
            "g\n",
            "h\n",
            "i\n",
            "j\n",
            "k\n",
            "l\n",
            "m\n",
            "n\n",
            "o\n",
            "p\n",
            "q\n",
            "r\n",
            "s\n",
            "t\n",
            "u\n",
            "v\n",
            "w\n",
            "x\n",
            "y\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 4\n",
        "n=1\n",
        "while n<100:\n",
        "  if(n%2==0):\n",
        "    print(n)\n",
        "  n+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lRmUzpgXUfJu",
        "outputId": "c122376e-5f32-4427-f393-58842d801919"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n",
            "22\n",
            "24\n",
            "26\n",
            "28\n",
            "30\n",
            "32\n",
            "34\n",
            "36\n",
            "38\n",
            "40\n",
            "42\n",
            "44\n",
            "46\n",
            "48\n",
            "50\n",
            "52\n",
            "54\n",
            "56\n",
            "58\n",
            "60\n",
            "62\n",
            "64\n",
            "66\n",
            "68\n",
            "70\n",
            "72\n",
            "74\n",
            "76\n",
            "78\n",
            "80\n",
            "82\n",
            "84\n",
            "86\n",
            "88\n",
            "90\n",
            "92\n",
            "94\n",
            "96\n",
            "98\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 5\n",
        "n=int(input(\"enter number\"))\n",
        "i=1\n",
        "c=0\n",
        "while i<n:\n",
        "  if(i%2!=0):\n",
        "    c=c+i\n",
        "  i+=1\n",
        "print(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q1bldkfFUoyt",
        "outputId": "d4c09ed4-a20c-49ff-ed20-4ed1d6301071"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number10\n",
            "25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 6\n",
        "n = int(input(\"enter number\"))\n",
        "count =0\n",
        "while n>0:\n",
        "  count+=1\n",
        "  n//=10\n",
        "print(count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KHIRK3UNVpg_",
        "outputId": "e45e8880-5282-4590-c2ae-3bd690af0db7"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number12345\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 7\n",
        "n = int(input(\"enter number\"))\n",
        "sum=0\n",
        "a=0\n",
        "while n>0:\n",
        "  a=n%10\n",
        "  sum=sum+a\n",
        "  n//=10\n",
        "print(sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BLD7mbG9V8Ou",
        "outputId": "96c9c5d2-c5d4-4b32-bfb5-51f69db91ec2"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number12345\n",
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 8\n",
        "n = int(input(\"enter number\"))\n",
        "a=n%10\n",
        "while n>1:\n",
        "  n//=10\n",
        "print(\"first number\", n)\n",
        "print(\"last digit\" , a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P2r8r83pWy5c",
        "outputId": "3e246bb2-84de-4b05-8256-84d5c02f707b"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number12345\n",
            "first number 1\n",
            "last digit 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 9\n",
        "n = int(input(\"enter number\"))\n",
        "a=n%10\n",
        "while n>1:\n",
        "  n//=10\n",
        "print(a+n)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kbrec3aPYxhS",
        "outputId": "f722c774-3db2-405c-917b-7f6e4dce9d6b"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number12345\n",
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 10\n",
        "n= int(input(\"enter the number for reverse \"))\n",
        "sum=0\n",
        "a=0\n",
        "while n>0:\n",
        "  a=n%10\n",
        "  sum=sum*10+a\n",
        "  n=n//10\n",
        "print(sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pPTbZ66LZSP6",
        "outputId": "520fc7d5-7a7b-4285-9514-820bc283f14d"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the number for reverse 12345\n",
            "54321\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 11\n",
        "n = int(input(\"enter the number \"))\n",
        "p = int(input(\"enter the power \"))\n",
        "a=1\n",
        "for i in range(p):\n",
        "    a=a*n\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PVEPsp9uZtmp",
        "outputId": "1a67420e-44ea-4878-c723-428ee8d05e4f"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the number 2\n",
            "enter the power 3\n",
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 12\n",
        "n = int(input(\"enter the number \"))\n",
        "for i in range(1,n+1):\n",
        "    if(n%i==0):\n",
        "        print(i)"
      ],
      "metadata": {
        "id": "pbrjAnzqbiFV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 13\n",
        "n = int(input(\"enter the number for factorial \"))\n",
        "f = 1\n",
        "for i in range(1,n+1):\n",
        "    f = f*i\n",
        "print(f)"
      ],
      "metadata": {
        "id": "ot7aALbbggBU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 14\n",
        "n = int(input(\"enter first number \"))\n",
        "p = int(input(\"enter second number \"))\n",
        "for i in range(1,n+1):\n",
        "    if(n%i==0 and p%i==0):\n",
        "      x=i\n",
        "    LCM= n*p//x\n",
        "print(LCM)\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BEJUlfNidgQ9",
        "outputId": "3f6716c5-8d4a-4584-afaa-b66adcad3141"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter first number 17\n",
            "enter second number 25\n",
            "425\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 15\n",
        "a=int(input(\"enter number to check prime or not: \"))\n",
        "b=0\n",
        "for i in range(2,a):\n",
        "  if(a%i==0):\n",
        "    print(\"not prime\")\n",
        "    break\n",
        "else:\n",
        "  b+=1\n",
        "if(b==1):\n",
        "  print(\"prime\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mHEHKWeueMGw",
        "outputId": "16c80210-9401-4030-f471-75a283f17bcc"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number to check prime or not: 12\n",
            "not prime\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qjjQ54Ryf998"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}