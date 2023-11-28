const TravelJournal = () => {
    const entries = [
        {
        image: "https://japanupclose.web-japan.org/files/100462016.jpeg",
        place: 'Japan',
        location: "Mount Fuji",
        date: '12 Jan, 2021 - 24 Jan, 2021',
        description: 'Mount Fuji is one of the tallest mountains in Japan, standing at 3,776 meters.',
        },
        {
        image: "https://media.architecturaldigest.com/photos/63d93cc1e12ae5dbc1f1f7aa/16:9/w_1920%2Cc_limit/GettyImages-982774858.jpg",
        place: 'Australia',
        location: "Sydney Opera House",
        date: '12 Jan, 2021 - 24 Jan, 2021',
        description: 'The Sydney Opera House is a world-renowned architectural masterpiece and a symbol of Australia.',
        },
        {
        image: "https://www.fjordtours.com/media/old/1169/geiranger_per_eide_fn_stort.jpg?anchor=center&mode=crop&width=1600&height=500&rnd=132417902460000000&slimmage=False",
        place: 'Geirangerfjord',
        location: "Norway",
        date: '27 May, 2021 - 8 Jun, 2021',
        description: 'Geirangerfjord is a stunning fjord in Norway, surrounded by majestic mountains and waterfalls.',
        },
    ];

return (
    <div className="travel-journal">
        <div className="entries">
        {entries.map((entry, index) => (
            <Entry key={index} {...entry} />
        ))}
        </div>
    </div>
    );
};

const Entry = ({ image, place, location, date, description }) => {
    return (
        <div className="entry">
        <img src={image} alt={place} />
        <div className="text-container">
            <h3>{place}</h3>
            <h2 className="location">{location}</h2>
            <p className="date">Date: {date}</p>
            <p className="description">{description}</p>
        </div>
        </div>

    );
};

export default TravelJournal;
