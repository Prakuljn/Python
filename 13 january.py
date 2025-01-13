{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQoisLsU05KaoL6OX4lVTJ"
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
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "Td2AcYBNHEq-",
        "outputId": "f361055b-b59c-4ae2-c553-0ac01a5d559b"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\n(j>  1 2 3 4 5)  \\ni\\n1     * * * * *\\n2     * * * * * \\n3     * * * * * \\n4     * * * * * \\n5     * * * * * \\n\\ni known as rows \\nj known as columns\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "# patterns through nested loops\n",
        "# basic pattern\n",
        "'''\n",
        "(j>  1 2 3 4 5)\n",
        "i\n",
        "1     * * * * *\n",
        "2     * * * * *\n",
        "3     * * * * *\n",
        "4     * * * * *\n",
        "5     * * * * *\n",
        "\n",
        "i known as rows\n",
        "j known as columns\n",
        "'''"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(1,6):\n",
        "        print(\"*\",end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gBlTO2m9J54J",
        "outputId": "c8dafaa8-3345-4c20-b89f-64265e89e8c9"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* * * * * \n",
            "* * * * * \n",
            "* * * * * \n",
            "* * * * * \n",
            "* * * * * \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(1,6):\n",
        "        print(i,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iGlvQkgfHJO_",
        "outputId": "03e34dee-29e3-4872-b37f-a5669e6d7d2a"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 1 1 1 1 \n",
            "2 2 2 2 2 \n",
            "3 3 3 3 3 \n",
            "4 4 4 4 4 \n",
            "5 5 5 5 5 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(1,6):\n",
        "        print(j,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LuVelJQYIn3Z",
        "outputId": "3661a26e-d029-4145-eac0-068ca82e1192"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 \n",
            "1 2 3 4 5 \n",
            "1 2 3 4 5 \n",
            "1 2 3 4 5 \n",
            "1 2 3 4 5 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=1\n",
        "for i in range(1,6):\n",
        "    for j in range(1,6):\n",
        "        print(a,end=\" \")\n",
        "        a+=1\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ToyE1nvJIsib",
        "outputId": "94963c23-6bd9-4770-f501-45d089011b84"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 \n",
            "6 7 8 9 10 \n",
            "11 12 13 14 15 \n",
            "16 17 18 19 20 \n",
            "21 22 23 24 25 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    a=4\n",
        "    for j in range(1,6):\n",
        "        print(a,end=\" \")\n",
        "        a+=2\n",
        "    print()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Pv2V2bwZJQ-U",
        "outputId": "44646143-9989-4013-85c4-9d1f87f85df0"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4 6 8 10 12 \n",
            "4 6 8 10 12 \n",
            "4 6 8 10 12 \n",
            "4 6 8 10 12 \n",
            "4 6 8 10 12 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5,0,-1):\n",
        "    for j in range(1,6):\n",
        "        print(i,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IzQldJZQJwFc",
        "outputId": "1233371b-a537-48c4-8547-e00b98572a9d"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 5 5 5 5 \n",
            "4 4 4 4 4 \n",
            "3 3 3 3 3 \n",
            "2 2 2 2 2 \n",
            "1 1 1 1 1 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(1,i+1):\n",
        "        print(\"*\",end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zWYMdIz2LmvB",
        "outputId": "8c129f1e-1e06-466d-b810-7afd117789fc"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* \n",
            "* * \n",
            "* * * \n",
            "* * * * \n",
            "* * * * * \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5,0,-1):\n",
        "    for j in range(1,i+1):\n",
        "        print(\"*\",end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qsREVglONdBq",
        "outputId": "d8709a83-0b72-4d55-b696-0b17904344a2"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* * * * * \n",
            "* * * * \n",
            "* * * \n",
            "* * \n",
            "* \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(1,6):\n",
        "        if(i==1 or i==5 or j==1  or j==5):\n",
        "          print(\"*\",end=\" \")\n",
        "        else:\n",
        "          print(\" \",end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IZplhNihNrEC",
        "outputId": "afdab493-8166-440f-8aeb-3b5fa840766a"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* * * * * \n",
            "*       * \n",
            "*       * \n",
            "*       * \n",
            "* * * * * \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(1,i+1):\n",
        "        print(j,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pfu922ltNuqu",
        "outputId": "9c270101-18f2-4f32-c2e0-90f2af0e4f5d"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 \n",
            "1 2 \n",
            "1 2 3 \n",
            "1 2 3 4 \n",
            "1 2 3 4 5 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5,0,-1):\n",
        "    for j in range(5,i-1,-1):\n",
        "        print(j,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yqbJEVXjOX_-",
        "outputId": "2c1c4380-4b95-4447-953c-ffb23e2cc468"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 \n",
            "5 4 \n",
            "5 4 3 \n",
            "5 4 3 2 \n",
            "5 4 3 2 1 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=10\n",
        "for i in range(1,6):\n",
        "    for j in range(1,i+1):\n",
        "        print(a,end=\" \")\n",
        "        a+=2\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OBzfJwtNOlVB",
        "outputId": "72c0543e-b7d4-45d6-a546-4d027add9261"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 \n",
            "12 14 \n",
            "16 18 20 \n",
            "22 24 26 28 \n",
            "30 32 34 36 38 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(5,i-1,-1):\n",
        "        print(j,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kTB9fhONO_YJ",
        "outputId": "96766ca0-ebfc-4908-b6a5-92b6a95cdb33"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 4 3 2 1 \n",
            "5 4 3 2 \n",
            "5 4 3 \n",
            "5 4 \n",
            "5 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5,0,-1):\n",
        "    for j in range(1,i+1):\n",
        "        print(j,end=\" \")\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ybkGpahzPIMq",
        "outputId": "911f2996-0848-4665-e457-bc5d5d6d91f3"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 \n",
            "1 2 3 4 \n",
            "1 2 3 \n",
            "1 2 \n",
            "1 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    a=65\n",
        "    for j in range(5,i-1,-1):\n",
        "        print(chr(a),end=\" \")\n",
        "        a+=1\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ORJ24konP1ts",
        "outputId": "08660e37-e919-4f0e-a90e-1f99c0399ad2"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A B C D E \n",
            "A B C D \n",
            "A B C \n",
            "A B \n",
            "A \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=65\n",
        "for i in range(1,6):\n",
        "    for j in range(5,i-1,-1):\n",
        "        print(chr(a),end=\" \")\n",
        "        a+=1\n",
        "    print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R6F_lJ1BQKJj",
        "outputId": "def8e747-078c-4bce-e42e-d755a262f392"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A B C D E \n",
            "F G H I \n",
            "J K L \n",
            "M N \n",
            "O \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,6):\n",
        "    for j in range(i,6):\n",
        "        print(\" \",end=\" \")\n",
        "    for k in range(1,i+1):\n",
        "        print(\"*\",end=\" \")\n",
        "    print()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nNXdSlIuQX92",
        "outputId": "ddb5f04c-d195-4ef0-f312-e254522aafe9"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          * \n",
            "        * * \n",
            "      * * * \n",
            "    * * * * \n",
            "  * * * * * \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Yo6Dfs0kTx0u"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}