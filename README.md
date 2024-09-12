# NGLx CLI

## Requirements

- Python 3.x
- Required packages: `httpx`, `colorama`

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/BrainlessDip/NGLx-CLI.git
   cd NGLx-CLI
   ```

2. **Install Dependencies:**

   Use pip to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Delay:**

   Edit the `config.json` file to set your desired delay between message submissions:

   ```json
   {
       "delay": 1.0  // Set the delay in seconds
   }
   ```

## Usage

1. **Run the Script:**

   Start the program by running:

   ```bash
   python nglx.py
   ```

2. **Follow the Prompts:**

   - Enter the target NGL username.
   - Specify the number of messages you want to send.
   - Enter the message content.

   The script will begin sending messages based on your inputs and display the progress in the console.

## Example

```bash
[~] Enter username: exampleuser
[~] Enter message count: 10
[~] Enter message: Hello from NGL Spammer!
```

## Web Version

For a more user-friendly experience, you can use the web version of this tool available at:

[NGLx Web Version](https://github.com/BrainlessDip/NGLx)

## Notes

- The script logs the status of each message sent, including successes, errors, and rate limits.
- Ensure you use this tool responsibly and within the terms of service of NGL.link.

## Disclaimer

This tool is for educational and testing purposes only. Misuse of this script to spam or harass is prohibited and may lead to legal consequences. Use responsibly.