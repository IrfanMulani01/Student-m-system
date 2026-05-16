// Sample Data
const recentGrades = [
    { subject: "Data Structures", score: "94", grade: "A+", date: "May 12" },
    { subject: "Operating Systems", score: "87", grade: "A", date: "May 10" },
    { subject: "Mathematics-IV", score: "76", grade: "B+", date: "May 8" },
];

function populateGrades() {
    const tbody = document.getElementById('gradesTable');
    tbody.innerHTML = '';
    
    recentGrades.forEach(grade => {
        const row = document.createElement('tr');
        row.className = 'border-b hover:bg-gray-50';
        row.innerHTML = `
            <td class="py-5">${grade.subject}</td>
            <td class="py-5 font-semibold">${grade.score}</td>
            <td class="py-5">
                <span class="px-4 py-1 bg-green-100 text-green-700 rounded-full text-xs font-medium">${grade.grade}</span>
            </td>
            <td class="py-5 text-gray-500">${grade.date}</td>
        `;
        tbody.appendChild(row);
    });
}

// Chart
let progressChart;
function createChart() {
    const ctx = document.getElementById('progressChart');
    
    if (progressChart) progressChart.destroy();
    
    progressChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['DSA', 'OS', 'DBMS', 'ML', 'Web Dev', 'CN'],
            datasets: [{
                label: 'Score (%)',
                data: [94, 87, 91, 78, 95, 82],
                backgroundColor: '#6366f1',
                borderRadius: 8,
                barThickness: 30,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    grid: { color: '#f3f4f6' }
                },
                x: {
                    grid: { color: '#f3f4f6' }
                }
            }
        }
    });
}

function setActive(el) {
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });
    el.classList.add('active');
}

function logout() {
    if (confirm("Are you sure you want to logout?")) {
        window.location.href = "#";
    }
}

// Initialize
window.onload = function() {
    populateGrades();
    createChart();
    
    // Tailwind script already loaded via CDN
    console.log("%cStudent Dashboard Loaded Successfully! 🎉", "color: #6366f1; font-size: 14px; font-weight: bold");
};
