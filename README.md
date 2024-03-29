# redditLinkScraper

Fetch and parse reddit data from pushshift.io to obtain a full collection of mynoise supergen metadata.

## TODOs
1. `get_pushshift.py` - Use date of last scrape or post Id to get only new posts ()
2. `parse_post_data.py`
  
    a. Save supergens to a file

    b. Load paths and filenames from a config module
3. `NoiseMachineService.py`
    
    a. Attempt to scrape meta of a single noise machine if not found in data file
4. `linkParser.py`
    
    a. Create regex to match links w/o link text
5. Make this work seamlessly with `supergen_scraper`

## Usage
### 1. Obtain data file from `supergen_scraper` project.
### 2. Run get_pushshift.py
  1. Fetches subreddit `posts` and `links` from pushshift.io
  2. Saves 1 batch per file to `/data/redditPostData/`

### 3. Run parse_post_data.py
  1. Reads each file in `/data/redditPostData/`
  2. Parses each link (easy)
  3. Parses each self-post (hairy)
      
      a. [ ] 1 or more supergen links
      
      b. [ ] Poorly titled within text
      
      c. [ ] Some lacking titles
      
      d. [ ] Invalid supergen link(s)
  4. Adds each submission to the SupergenService
  5. Saves via SupergenService to `/data/output/`

### 4. Harvest `/data/output/`
TBD

## Classes

### SupergenService
The interface for adding to and saving to the repository.

Functions:

**add** - Attempts to create and add a supergen to the underlying repository

**save_all** - Saves changes to the repository

Dependencies:
1. NoiseMachineService.py
2. SupergenFactory.py
3. SupergenRepository.py

### SupergenRepository
Array wrapper that saves to `/data/output/supergenPosts.json`

Functions:

**try_add_supergen** - Adds to array

**save_all** - Saves array to file

Dependencies:
1. fileIo.py
2. logger.py

### NoiseMachineService
Reads and serves up noise generator data from a file.
This data file is generated and hydrated by the `supergen_scraper` project.

Functions:

**get_noise_machines(url)** - Finds noise machines that are referenced in a supergen's url

Dependencies:
1. logger
2. json
3. re
4. urllib.parse
5. hydrated noise generated data file

### SupergenFactory
Creates and returns a supergen json object

Functions:

**create** - Creates a supergen
  * post_id
  * author
  * created_utc
  * reddit_url - permalink to original post
  * url - url of the supergen
  * title
  * noise_machines - list of noise machine meta objects

Dependencies:
1. logger
2. json

## Modules
### fileIo
Functions: 

**list_dir(path)** - wrapper for os.listdir
**read_json(file_name)** - reads and returns data for given file
**try_write_array** - writes an array to file

Dependencies:
1. os
2. json

### linkParser
Functions:

**find_all_titled_links(self_text)** - returns all regex matches for supergen links prefixed with a title

**find_all_untitled_links(self_text)** - returns all regex matches for supergens without titles

Dependencies:
1. re

### logger
Appends to a log file

Functions:

**error** - logs with error level

**warn** - logs with warn level

**info** - logs with info level

Dependencies:
1. datetime
