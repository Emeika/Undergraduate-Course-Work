#ifndef media_H
#define media_H

using namespace std;
#include <string>

class Media
{
private:
    string title, author;

public:
    Media(string title, string author); // Constructor

    // getters to access in inherited classes (not really needed for this code)
    string get_title();

    string get_author();

    void display();
};

class Audio : public Media // Inherited from Media class
{
private:
    float audio;

public:
    // Constructor
    Audio(string title, string author, float audio);

    void display();
};

class Video : public Media // Inherited from Media class
{
private:
    int resolution;

public:
    Video(string title, string author, int resolution);
    void display();
};

class Text : public Media
{
private:
    int wordCount;

public:
    Text(string title, string author, int wordCount);

    void display();
};

#endif