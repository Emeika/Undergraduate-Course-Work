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

MediaLibrary::MediaLibrary(int size) : size(size), library(new Media *[size]) {} // dynamically allocated array of Media* pointers

MediaLibrary::~MediaLibrary()
{ // To free memory allocated
    for (int i = 0; i < size; i++)
    {
        delete library[i];
    }
    delete[] library;
}
void MediaLibrary::addMedia(Media *m)
{
    static int i = 0; // counter
    if (i < size)
    {
        library[i] = m; // adding object at index i
        i++;            // increment
    }
}

void MediaLibrary::displayLibrary()
{
    for (int i = 0; i < size; i++)
    {                          // loop for each media object
        library[i]->display(); // dereferences the pointer and calls the display() method object it points to.
        cout << endl;
    }
}
