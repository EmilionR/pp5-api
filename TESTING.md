# Table of Contents
* [Validator Testing](#validator-testing)
  * [Python](#python)
* [Manual Testing](#manual-testing)
* [DRF API](#drf-api)
* [Profiles](#profiles)
* [Posts](#posts)
* [Comments](#comments)
* [Followers](#followers)

## Validator Testing

### Python

All Python files were run validated with pep8 and cleaned until no errors were found.

<details>
<summary>Python validation results</summary>

![Python validation](documentation/pep8.png)
</details>

## Manual Testing

### DRF API
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
| Refresh token | POST | Refreshes the auth token to keep the user signed in | Pass |
| Sign-out view | POST | Destroys the token and signs the user out | Pass |

### Profiles
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
| Profile List | GET | Show a list of all profiles as JSON objects | Pass |
| Profile List | POST | Create a new profile if valid | Pass |
| Profile List | POST | Automatically make a profile when creating a user | Pass |
| Profile Detail | GET | Return a specific profile if given a valid id | Pass |
| Profile Detail | POST | Create a new | Pass |
| Profile Detail | PUT | Update the profile if valid | Pass |
| Profile Detail | DELETE | Destroy the profile and its owner instance if valid | Pass |
| Related instances | DELETE | Destroying a profile destroys all content related to its owner | Pass |

### Posts
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
| Post List | GET | Show a list of all posts as JSON objects | Pass |
| Post List | POST | Create a new post if valid | Pass |
| Post Detail | GET | Return a specific post if given a valid id | Pass |
| Post Detail | POST | Create a new post if valid | Pass |
| Post Detail | PUT | Update the post if valid | Pass |
| Post Detail | DELETE | Destroy the post instance if valid | Pass |

### Comments
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
| Comment List | GET | Show a list of all comments as JSON objects | Pass |
| Comment List | POST | Create a new comment if valid | Pass |
| Comment Detail | GET | Return a specific comment if given a valid id | Pass |
| Comment Detail | POST | Create a new comment if valid | Pass |
| Comment Detail | PUT | Update the comment if valid | Pass |
| Comment Detail | DELETE | Destroy the comment if valid | Pass |

### Followers
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Likes
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Friends
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Blocks
| Feature | Action | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Reports