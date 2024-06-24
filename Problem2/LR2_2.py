{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5443e9e1-2edb-4592-a82b-c744ce6e918a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the filename:  test1.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The file has 5 lines.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a line number (0 to quit):  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Line 3: asdgfasfdas\n",
      "\n",
      "The file has 5 lines.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a line number (0 to quit):  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting program.\n"
     ]
    }
   ],
   "source": [
    "def read_file_lines(filename):\n",
    "    \"\"\"Read lines from a file and return as a list.\"\"\"\n",
    "    try:\n",
    "        with open(filename, 'r') as file:\n",
    "            return file.readlines()\n",
    "    except FileNotFoundError:\n",
    "        print(f\"Error: File '{filename}' not found.\")\n",
    "        return None\n",
    "\n",
    "def main():\n",
    "    # Prompt user for filename\n",
    "    filename = input(\"Enter the filename: \")\n",
    "    \n",
    "    # Read lines from the file\n",
    "    lines = read_file_lines(filename)\n",
    "    \n",
    "    if lines is None:\n",
    "        return\n",
    "    \n",
    "    # Remove newline characters from the end of each line\n",
    "    lines = [line.strip() for line in lines]\n",
    "    \n",
    "    # Main loop\n",
    "    while True:\n",
    "        # Print the number of lines in the file\n",
    "        print(f\"\\nThe file has {len(lines)} lines.\")\n",
    "        \n",
    "        # Prompt user for line number\n",
    "        try:\n",
    "            line_number = int(input(\"Enter a line number (0 to quit): \"))\n",
    "        except ValueError:\n",
    "            print(\"Please enter a valid integer.\")\n",
    "            continue\n",
    "        \n",
    "        # Check if user wants to quit\n",
    "        if line_number == 0:\n",
    "            print(\"Exiting program.\")\n",
    "            break\n",
    "        \n",
    "        # Print the requested line\n",
    "        if 1 <= line_number <= len(lines):\n",
    "            print(f\"Line {line_number}: {lines[line_number - 1]}\")\n",
    "        else:\n",
    "            print(f\"Error: Line number must be between 1 and {len(lines)}.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3eb407f-44fc-479b-863f-df3881148d69",
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
