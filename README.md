# NGLx CLI
![Preview Image](https://i.ibb.co.com/0pmjn5Lt/Screenshot-2025-04-04-134841.png)
## Prerequisites

- **Python 3.x** installed on your system.
- Required Python packages: `httpx`, `colorama`.

## Installation Guide

1. **Clone the Repository:**

   Begin by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/BrainlessDip/NGLx-CLI.git
   cd NGLx-CLI
   ```

2. **Install Required Dependencies:**

   Install the necessary Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Delay:**

   Modify the `config.json` file to set your preferred delay (in seconds) between message submissions:

   ```json
   {
       "delay": 0.5, // Delay in seconds
       "lastUsername": "dip",
       "lastCount": 18
   }
   ```

## Usage Instructions

1. **Launch the Script:**

   Execute the script by running the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Follow the On-Screen Prompts:**

   - **Username:** Enter the target NGL username. If you press Enter without typing, the script will use the last saved username.
   - **Message Count:** Specify the number of messages you wish to send. Press Enter to use the last saved count.
   - **Message Content:** Enter the message you want to send. If you press Enter without typing, the script will randomly select a question from `questions.txt`

   The script will automatically save your last-used username and message count for future sessions

3. **Random Questions:**

   To send random questions, ensure your questions are listed in the `questions.txt` file, with each question on a new line. When prompted for the message, simply press Enter, and the script will randomly select a question from the file

## Example Workflow

```bash
[~] Enter username (username): dip
[~] Enter message count (27): 37
[!] Press Enter for random questions
[~] Enter message:
```

## Web Version

For a more intuitive and user-friendly experience, you can use the web version of this tool, available at:

[NGLx Web Version](https://github.com/BrainlessDip/NGLx)

## Disclaimer

This tool is designed strictly for educational and testing purposes. Use it responsibly and ensure you have permission from the target user before sending messages. Misuse of this tool is not encouraged and is solely the responsibility of the user