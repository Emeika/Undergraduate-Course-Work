#include <iostream>
#include "media.h"

using namespace std;

Media::Media(string title, string author) : title(title), author(author) {} // Constructor

// getters
string Media::get_title() { return title; }

string Media::get_author() { return author; }

void Media::display()
{
    cout << "Title: " << title << endl;
    cout << "Author: " << author << endl;
}

// Constructor
Audio::Audio(string title, string author, float audio) : Media(title, author), audio(audio) {}

void Audio::display()
{
    Media::display(); // Inherit function from base class
    cout << "Audio: " << audio << endl;
}

Video::Video(string title, string author, int resolution) : Media(title, author), resolution(resolution) {}

void Video::display()
{
    Media::display();
    cout << "Resolution: " << resolution << endl;
}

Text::Text(string title, string author, int wordCount) : Media(title, author), wordCount(wordCount) {}

void Text::display()
{
    Media::display(); // override display
    cout << "Number of words: " << wordCount << endl;
}
