<p align="center">    <a href="https://github.com/probably-human/papayaseason" alt="Papaya Season Logo">
    <img src="icons/logo_110px.png"/></a></p><h1 align="center"> Papaya Season </h1>

<h4 align="center"> Qt-based GUI app that suggests the best time to eat papaya <br /> depending on where it was grown</h4>

<h4 align="center"> Python 3.10, PyQt5</h4>

## Why Papaya Season?

Many people know **how and when** it’s best to eat their local fruits.
But what about fruits that may **not grow local** to you - for example papayas? 
It would be a pity if people would end up to not liking the fruit, or might even throw it away. 
Papaya Season wants to help with this issue by providing the **harvest time** based on the country the papaya is from. 
This gives you the prerequisite to **enjoy** my favourite fruit as well.

## Screen Recording

<img src="icons/screenrecording_for_readme.gif" alt="Papaya Season Screen Recording"/>

## Code overview

frame_1: Home - from here you can start the app

frame_2: The code allows a flexible number of buttons. It creates as many buttons, as there are countries in the json-file. The buttons are filled with data from the json-file (name of the countries).

frame_3: Based on the user’s choice, the app creates a unique answer and displays an animation to emphasize the given answer. Depending on which month it is, the app will check if it is papaya season in the chosen country, or not. The app will show a confirming animation and text if it is papaya season. Otherwise, it will show a warning animation and text. The user can click the “Try another country”-button to go back to frame_2 and choose another button.

## Data
For this app I've researched harvest times in several countries and tried to make the data as realistic as possible. But the data should still be considered as testdata.

## Credits
Thanks to: <a href="https://github.com/MariyaSha/TriviaGame">MariyaSha’s Trivia Game</a> app which served as a template for this app

Animations: The animations are made with <a href="https://www.canva.com">Canva</a>'s free content license

Font: <a href = "https://github.com/ossobuffo/didact-gothic">Didact Gothic</a> by <a href="https://github.com/ossobuffo">ossobuffo</a>