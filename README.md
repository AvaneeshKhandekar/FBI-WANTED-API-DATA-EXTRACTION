## FBI WANTED API DATA EXTRACTION

### AUTHOR

Name: Avaneesh Khandekar

### INSTALLATION

To Install required dependencies: `pipenv install -e`

### USAGE

To fetch data from the given page number using the FBI API:

`pipenv run python main.py --page <integer>`

To fetch data from a local json:

`pipenv run python main.py --file <file-location>`

### OVERVIEW

This script fetches data from the FBI API:  https://www.fbi.gov/wanted/api \
It parses the response in json and extracts 3 fields from the response:

- Title - Single String
- Subject - List of Strings
- Field Office - List of Strings\
  The extracted data is then formatted in the specified format:\
  `{title}þ{subjects}þ{field_offices}`\

Once, formatted the result is printed to console line by line for each item retrieved from the API.\

This script also has the functionality to extract data directly from a JSON that matches the format of the FBI API. (In
this case no API call is made/ local file is used instead)

### FUNCTIONS

#### `fetch_details_from_api(page_number)`

- **Description**: Fetch data from the FBI API with a specific page number.
- **Params**:
    - `page_number` (integer): Page Number to get from API.
- **Returns**: Formatted data as specified above.

#### `fetch_details_local(file_path)`

- **Description**: Fetch Data from a JSON file.
- **Params**:
    - `file_path` (string): Path of the local json file.
- **Returns**: Formatted data as specified above.

#### `format_data(data)`

- **Description**: Formats Raw JSON data, Creates a string for all items with fields separated using the thorn
  character.
- **Params**:
    - `data` (json): Json data containing "items", "title", "subjects", AND "field_offices".
- **Returns**: List of formatted strings.

#### `print_data(data)`

- **Description**: Prints the formatted data line by line.
- **Params**:
    - `data` (list): LIST OF Strings.
- **Returns**: None, prints to STD OUT.

### BUGS & ASSUMPTIONS:

- **Valid Data Format**: It is assumed that data from the api and also the local json is structured correctly.
- **Valid Input Range**: It is assumed that user knows the page range of the API key. In case of a non-existed page,
  program will output a message stating no data found.
- **Authorization/Rate Limit**: It is assumed that FBI API call iss public and no authorization is required to call it,
  no rate limit will be applied.
- **URL**: It is assumed that the URL is correct and does not change.
