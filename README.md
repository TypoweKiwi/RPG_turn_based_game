## RPG Turn-Based Game 

A console-based turn-based RPG built in Python, featuring an interactive interface powered by PyInquirer for choice-based navigation and Rich for colorful panels and dynamic terminal output. This project was created to practice object-oriented programming, clean code principles, working with a larger project structure, and building architecture with scalability and extensibility in mind.

## Gameplay overview

The game places you in charge of a party of up to four heroes, each belonging to a unique class with distinct abilities (Currently, there are 2 hero classes available). Your adventure begins in the Adventure Hub — a central place where you can recruit heroes in the Tavern, buy maps, buy equipment in the Shop, heal your party in the Temple, and manage your characters' inventory (The party shares a common stash for collective resources, while each hero also maintains their own personal inventory for equipment and items).

Once prepared, you set out on expeditions into procedurally generated dungeons, where you’ll battle enemies, collect loot, and earn experience. The length and difficulty of each dungeon depend on both the type of map you choose and the number of previously completed dungeons. While exploring, you can encounter combat rooms, where your party must fight to progress, as well as safe rooms that offer various interactive events. Every tenth dungeon culminates in a challenging boss encounter (yet not implemented) that tests the strength and strategy of your team.

Heroes grow stronger as they gain experience and gear, and your progress is preserved through a save/load system, allowing you to continue your adventure across multiple sessions. Saving and loading are only available in the Adventure Hub, between dungeon expeditions.

## Requirements/Installation

* **Language:** Python 3.x  
* **Dependencies:**
  * `PyInquirer` - interactive console interface  
  * `Rich` - colorful terminal UI  
  * `os`, `datetime`, `enum` – built-in Python modules  

Install the required libraries using `pip`.

## Running the Game

To start the game, simply type in your IDE terminal:
`python main.py`

## Future Improvements
Planned features and enhancements include:
* Adding more hero classes  
* Expanding the pool of items and equipment  
* Introducing additional monster types  
* Implementing the boss encounter system  
* Reworking safe room encounters  
* Improving in-game messages and feedback text  
* Expanding and balancing the skill system  