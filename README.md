# GD Code to Level
This Python script allows you to programmatically place objects in a Geometry Dash level using the gd module. The script reads object data from a CSV file and uploads it to the Geometry Dash server.

## CSV File Format
The CSV file should be formatted as follows:

Copy code
block_id;x_position;y_position
block_id: The ID of the object to be placed. This can be obtained from the Geometry Dash editor or the gd module's documentation.
x_position: The desired x-coordinate position for the object.
y_position: The desired y-coordinate position for the object.
Each row in the CSV file represents a single object placement.

## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.