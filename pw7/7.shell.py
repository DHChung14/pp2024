import subprocess
import sys

def execute_command(command):
    """Executes the command and handles I/O redirection."""
    # Split the command to handle arguments and redirection
    command_parts = command.split()
    
    # Handle input redirection (<)
    if '<' in command_parts:
        input_index = command_parts.index('<')
        input_file = command_parts[input_index + 1]
        command_parts = command_parts[:input_index]  # Remove redirection part
        input_stream = open(input_file, 'r')
    else:
        input_stream = sys.stdin  # Default input is stdin
    
    # Handle output redirection (>)
    if '>' in command_parts:
        output_index = command_parts.index('>')
        output_file = command_parts[output_index + 1]
        command_parts = command_parts[:output_index]  # Remove redirection part
        output_stream = open(output_file, 'w')
    else:
        output_stream = sys.stdout  # Default output is stdout

    # Handle pipes (|)
    if '|' in command_parts:
        # Split the command by pipe
        pipe_index = command_parts.index('|')
        first_command = command_parts[:pipe_index]
        second_command = command_parts[pipe_index + 1:]

        # Execute the first command
        p1 = subprocess.Popen(first_command, stdout=subprocess.PIPE, stdin=input_stream)
        # Execute the second command with the output of the first command as input
        p2 = subprocess.Popen(second_command, stdin=p1.stdout, stdout=output_stream)

        # Wait for the second command to finish
        p2.communicate()
    else:
        # No pipe, just execute the command normally
        subprocess.run(command_parts, stdin=input_stream, stdout=output_stream)

    # Close input/output files if opened
    if input_stream is not sys.stdin:
        input_stream.close()
    if output_stream is not sys.stdout:
        output_stream.close()

def main():
    """Main shell loop to handle user input and commands."""
    while True:
        # Display the shell prompt
        command = input("Shell> ").strip()
        
        if command.lower() == 'exit':
            print("Exiting shell.")
            break
        
        try:
            execute_command(command)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
