{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMfvcNcVVIVKJlvKyC4f/nd",
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
        "<a href=\"https://colab.research.google.com/github/Prakuljn/Python-Assignment/blob/main/10%20january.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-n8q6EF-lYS2",
        "outputId": "e99410c2-9f00-402c-ecc1-4665e22aa4f2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "number is divisable by 2 6 and 7 42\n",
            "number is divisable by 2 6 and 7 44\n",
            "number is divisable by 2 6 and 7 46\n",
            "number is divisable by 2 6 and 7 48\n",
            "number is divisable by 2 6 and 7 50\n",
            "number is divisable by 2 6 and 7 52\n",
            "number is divisable by 2 6 and 7 54\n",
            "number is divisable by 2 6 and 7 56\n",
            "number is divisable by 2 6 and 7 58\n",
            "number is divisable by 2 6 and 7 60\n",
            "number is divisable by 2 6 and 7 62\n"
          ]
        }
      ],
      "source": [
        "num =42\n",
        "count = 0\n",
        "while count <= 10:\n",
        "  if (num%2==0 and num%2==0 and num%2==0 ):\n",
        "    print(\"number is divisable by 2 6 and 7\" , num)\n",
        "    count+=1\n",
        "  num+=1\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=3\n",
        "b=7\n",
        "num=1\n",
        "while(True):\n",
        "  if(num%a==0 and num%b==0):\n",
        "    print(\"Divisable \" ,num)\n",
        "    break\n",
        "  num+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1qhzsVlqnWA4",
        "outputId": "50ab1537-c8b0-4d4d-d787-58c082c0958c"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Divisable  21\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input(\"Enter first number: \"))\n",
        "b = int(input(\"Enter second number: \"))\n",
        "c=0\n",
        "if(a<b):\n",
        "  c=b\n",
        "else:\n",
        "  c=a\n",
        "while(True):\n",
        "  if(c%a==0 and c%b==0):\n",
        "    print(\"lcm is\" , c)\n",
        "    break\n",
        "  c+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TnfwKSTUoDmJ",
        "outputId": "4542fd85-4bc8-4881-992a-0ab8f7e605f1"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 9\n",
            "Enter second number: 5\n",
            "lcm is 45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# palindrome number and string\n",
        "# the value or string from right side and left side is same\n",
        "# for example naman ,121 ,1234321\n",
        ""
      ],
      "metadata": {
        "id": "2xfDxonCqIz-"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data= input(\"enter the string to check palinndrome  \")\n",
        "start=0\n",
        "end=len(data)-1\n",
        "x=0\n",
        "while(start<end):\n",
        "  if(data[start]!=data[end]):\n",
        "    x+=1\n",
        "    break\n",
        "  start+=1\n",
        "  end-=1\n",
        "if(x!=1):\n",
        "  print(\"palindrome\")\n",
        "else:\n",
        "  print(\"not a palinndromme\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-ae8Re-oubv5",
        "outputId": "7137eeb4-e12b-4842-e679-815f51ddbaf0"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the string to check palinndrome  sarras\n",
            "palindrome\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data= input(\"enter the string to check palinndrome\")\n",
        "if(data==data[::-1]):\n",
        "  print(\"palindrome\")\n",
        "else:\n",
        "  print(\"not a palinndromme\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b9zfse2Cxowx",
        "outputId": "cd616fb6-a58c-4115-8844-78d7eaf4cb2b"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the string to check palinndromenester\n",
            "not a palinndromme\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# nested loops\n",
        "# loop inside the loop is called nested loop\n",
        "# mostly used in patterns\n",
        "for i in range(0,5):\n",
        "  print('employee', i)\n",
        "  for j in range(1,i+1):\n",
        "    print(\"food coupoun\" ,j)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nPMdNrhC1PMZ",
        "outputId": "9017564f-1a03-4689-aeac-ab25879d1086"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "employee 0\n",
            "employee 1\n",
            "food coupoun 1\n",
            "employee 2\n",
            "food coupoun 1\n",
            "food coupoun 2\n",
            "employee 3\n",
            "food coupoun 1\n",
            "food coupoun 2\n",
            "food coupoun 3\n",
            "employee 4\n",
            "food coupoun 1\n",
            "food coupoun 2\n",
            "food coupoun 3\n",
            "food coupoun 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num =5\n",
        "for i in range(1,5):\n",
        "  print('employee', i)\n",
        "  for j in range(num,1,-1):\n",
        "    print(\"food coupoun\" )\n",
        "  num-=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SyJSb7g519Au",
        "outputId": "18118b8f-3088-4164-8f9f-e8aa6664a7a0"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "employee 1\n",
            "food coupoun\n",
            "food coupoun\n",
            "food coupoun\n",
            "food coupoun\n",
            "employee 2\n",
            "food coupoun\n",
            "food coupoun\n",
            "food coupoun\n",
            "employee 3\n",
            "food coupoun\n",
            "food coupoun\n",
            "employee 4\n",
            "food coupoun\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"enter number\"))\n",
        "for i in range(1,11):\n",
        "   print(num*i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ic6TkNtt4xvb",
        "outputId": "b77872ef-4fe7-45ee-dc32-eb60872a0277"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number5\n",
            "5\n",
            "10\n",
            "15\n",
            "20\n",
            "25\n",
            "30\n",
            "35\n",
            "40\n",
            "45\n",
            "50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for num in range(2,7):\n",
        "  for i in range(1,11):\n",
        "    print(num*i , end =\" \")\n",
        "  print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FNslNKv-57aT",
        "outputId": "a5f8d03c-607e-43eb-e5b0-32e43c7b3c0b"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 4 6 8 10 12 14 16 18 20 \n",
            "3 6 9 12 15 18 21 24 27 30 \n",
            "4 8 12 16 20 24 28 32 36 40 \n",
            "5 10 15 20 25 30 35 40 45 50 \n",
            "6 12 18 24 30 36 42 48 54 60 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 8\n",
        "y = 3\n",
        "z = 5\n",
        "if x > y and y < z:\n",
        "    if y > z:\n",
        "        print(\"Y is the middle\")\n",
        "    else:\n",
        "        print(\"Z is the middle\")\n",
        "else:\n",
        "    print(\"X is not the largest\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qAniawvD6SCf",
        "outputId": "99383430-4116-4617-9bf0-8904edfef189"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Z is the middle\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#9. What will be the output of this code?\n",
        "x = 5;\n",
        "y = 5;\n",
        "z = 8;\n",
        "if x == y or y == z:\n",
        "    print(\"Condition True\")\n",
        "else:\n",
        "    print(\"Condition False\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HvxX15jq9wKN",
        "outputId": "b31927c3-d837-4a91-fb86-14efe445da89"
      },
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Condition True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "i-1KEB96_VYp"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}