{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPm77rHBXzKG7Hwe3h7pzJ4",
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
        "<a href=\"https://colab.research.google.com/github/Prakuljn/Python-Assignment/blob/main/09%20january%20for%20loop%20pratice.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zC-3-Y-xcVSt",
        "outputId": "94a52eb9-ab56-48f9-840c-db615648da21"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "p\n",
            "r\n",
            "a\n",
            "k\n",
            "u\n",
            "l\n",
            "j\n",
            "a\n",
            "i\n",
            "n\n"
          ]
        }
      ],
      "source": [
        "data= \"prakuljain\"\n",
        "for i in range(len(data)):\n",
        "    print(data[i])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "str=input(\"enter the string: \")\n",
        "for i in range(len(str)):\n",
        "    if(str[i]==\"a\" or str[i]==\"e\" or str[i]==\"i\" or str[i]==\"o\" or str[i]==\"u\"):\n",
        "        print(str[i])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O671X4OUeNr1",
        "outputId": "67ed9fc0-1976-481b-fa04-60c3cd817a22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the stringhello\n",
            "e\n",
            "o\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "count=0\n",
        "str=input(\"enter the string: \")\n",
        "for i in range(len(str)):\n",
        "    if(str[i]!=\"a\" or str[i]!=\"e\" or str[i]!=\"i\" or str[i]!=\"o\" or str[i]!=\"u\"):\n",
        "      count+=1\n",
        "print(count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7LuvM2yQel-U",
        "outputId": "1b11d0bd-0912-4f6f-fe69-6d37e3522bdc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the string: ALSKFDJSA\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "str=input(\"enter the string: \")\n",
        "for i in range ((len(str))//2):\n",
        "  print(str[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9ULB0uREjfyB",
        "outputId": "70bbb71b-fcee-4dba-831d-5f604ac29a61"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the string: prakul\n",
            "p\n",
            "r\n",
            "a\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,21):\n",
        "  if (i%3==0):\n",
        "    continue\n",
        "  else:\n",
        "    print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lyswFdotlbj2",
        "outputId": "9eccc187-1ac4-478c-a6e9-a54f2a8eccb0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "4\n",
            "5\n",
            "7\n",
            "8\n",
            "10\n",
            "11\n",
            "13\n",
            "14\n",
            "16\n",
            "17\n",
            "19\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
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
        "id": "D7i7BOlGmpfc",
        "outputId": "56e75887-b1b3-43f4-ecc7-5e515314c9bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number to check prime or not: 13\n",
            "prime\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# while loop\n",
        "''' we use for for loop for finite iritatetation\n",
        "    while for infinite iteration '''\n",
        ""
      ],
      "metadata": {
        "id": "Q2bu0_o2pNo1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "9f06472f-091e-43e1-dc34-b8e20f1358dd"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "' we use for for loop for finite iritatetation \\n    while for infinite iteration '"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=0\n",
        "b=1\n",
        "while a<5:\n",
        "  if(b%3==0):\n",
        "    print(b)\n",
        "    a+=1\n",
        "  b+=1\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZZRDI8vitZEa",
        "outputId": "16aafc0c-3a9b-48f2-d2e0-a196f62fbf99"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "6\n",
            "9\n",
            "12\n",
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=8\n",
        "b=a\n",
        "while a<100:\n",
        "  a=a+b\n",
        "  b+=1\n",
        "  print(b)\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UHsvn_mtupzd",
        "outputId": "cfb49d77-b42a-422c-ee02-ebd435c49065"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n",
            "10\n",
            "11\n",
            "12\n",
            "13\n",
            "14\n",
            "15\n",
            "16\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "f9Fpjwh6wADF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}