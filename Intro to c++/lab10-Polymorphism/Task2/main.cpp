
#include <iostream>
#include "media.h"
#include "media.cpp"

int main()
{
    MediaLibrary myLibrary(3);
    myLibrary.addMedia(new Audio("My Audio", "Audio Creator", 320));
    myLibrary.addMedia(new Video("My Video", "Video Creator", 1920));
    myLibrary.addMedia(new Text("My Text", "Text Creator", 1000));

    std::cout << "Displaying Media Library:" << std::endl;
    myLibrary.displayLibrary();

    return 0;
}
