const teachersData = [
    { name: 'Dr. Saba Khalil Toor', phone: '360', email: 'sabakhalil@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Dr-Saba-Khalil-Toor-scaled.jpg' },
    { name: 'Dr. Aasia Khanum', phone: '360', email: 'aasiakhanum@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Dr.-Aasia-Khanum-scaled.jpg' },
    { name: 'Dr. Mubashar Mushtaq', phone: '360', email: 'mubasharmushtaq@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Dr-Mubashar-Mushtaq-scaled.jpg' },
    { name: 'Dr. Maria Tamoor', phone: '360', email: 'mariatamoor@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Maria-Tamoor-scaled.jpg' },
    { name: 'Dr. Nosheen Sabahat', phone: '360', email: 'nosheensabahat@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Nosheen-Sabahat-scaled.jpg' },
    { name: 'Dr. Muhammad Salman Chaudhry', phone: '360', email: 'salmanchaudhry@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Muhammad-Salman-Chaudhry-scaled.jpg' },
    { name: 'Dr. Sarwan Altaf Abbasi', phone: '360', email: 'sarwanabbasi@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Dr-Sarwan-Altaf-Abbasi-scaled.jpg' },
    { name: 'Dr. Sidra Minhas', phone: '360', email: 'sidraminhas@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Sidra-Minhas-scaled.jpg' },
    { name: 'Dr. Saad Bin Saleem', phone: '360', email: 'saadsaleem@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Saad-Bin-Saleem-scaled.jpg' },
    { name: 'Dr. Umber Nisar', phone: '360', email: 'umbernisar@fccollege.edu.pk', image: 'https://www.fccollege.edu.pk/wp-content/uploads/Ambar-Nisar-scaled.jpg' }

];

const Teachers = () => {
    return (
        <div className="teachers-container">
        {teachersData.map((teacher, index) => (
            <div className="teacher-card" key={index}>
            <img src={teacher.image} alt={teacher.name} />
            <div className="card-details">
                <h3>{teacher.name}</h3>
                <p>📞 {teacher.phone}</p>
                <p>✉️{teacher.email}</p>
            </div>
            </div>
        ))}
        </div>
    );
};

export default Teachers;
