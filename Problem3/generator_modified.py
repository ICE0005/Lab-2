{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6f49f8be-0e9b-42a2-9c7c-b5b19f1ac1f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number of sentences:  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A GIRL THINK A BOY AT THE BAT\n",
      "A BOY DRIVE A BAT OVER THE GIRL\n",
      "THE GIRL DRIVE A BAT ON A BALL\n",
      "THE BOY SERVE THE BOY IN THE BAT\n",
      "A GIRL THINK THE BAT IN THE GIRL\n",
      "THE BOY SERVE A BOY UNDER A BALL\n",
      "THE BALL STOP THE BOY IN THE GIRL\n",
      "A GIRL DRIVE A GIRL ON THE BALL\n",
      "A GIRL STOP A BOY AT A BALL\n",
      "THE BAT DRIVE THE BOY OVER THE GIRL\n",
      "THE GIRL THINK THE BALL AT A BAT\n",
      "A BALL STOP THE GIRL AT A GIRL\n",
      "A BAT STOP A BAT ON A BAT\n",
      "A GIRL STRETCH THE BAT AT THE BALL\n",
      "A BALL STOP THE BOY UNDER THE BOY\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def getWords(filename):\n",
    "    \"\"\"\n",
    "    Reads words from a file and returns them as a tuple.\n",
    "    \n",
    "    :param filename: The name of the file to read from\n",
    "    :return: A tuple containing the words from the file\n",
    "    \"\"\"\n",
    "    temp_list = []\n",
    "    with open(filename, 'r') as file:\n",
    "        for line in file:\n",
    "            word = line.strip().upper()\n",
    "            if word:\n",
    "                temp_list.append(word)\n",
    "    return tuple(temp_list)\n",
    "\n",
    "# Load vocabulary from files\n",
    "articles = getWords('articles.txt')\n",
    "nouns = getWords('nouns.txt')\n",
    "verbs = getWords('verbs.txt')\n",
    "prepositions = getWords('prepositions.txt')\n",
    "\n",
    "def sentence():\n",
    "    \"\"\"Builds and returns a sentence.\"\"\"\n",
    "    return nounPhrase() + \" \" + verbPhrase()\n",
    "\n",
    "def nounPhrase():\n",
    "    \"\"\"Builds and returns a noun phrase.\"\"\"\n",
    "    return random.choice(articles) + \" \" + random.choice(nouns)\n",
    "\n",
    "def verbPhrase():\n",
    "    \"\"\"Builds and returns a verb phrase.\"\"\"\n",
    "    return random.choice(verbs) + \" \" + nounPhrase() + \" \" + \\\n",
    "           prepositionalPhrase()\n",
    "\n",
    "def prepositionalPhrase():\n",
    "    \"\"\"Builds and returns a prepositional phrase.\"\"\"\n",
    "    return random.choice(prepositions) + \" \" + nounPhrase()\n",
    "\n",
    "def main():\n",
    "    \"\"\"Allows the user to input the number of sentences\n",
    "    to generate.\"\"\"\n",
    "    number = int(input(\"Enter the number of sentences: \"))\n",
    "    for count in range(number):\n",
    "        print(sentence())\n",
    "\n",
    "# The entry point for program execution\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fedb022b-f89e-4c00-841d-2193738a1b43",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
