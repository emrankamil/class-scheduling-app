const departmentsData_url = 'http://localhost:8000/api/departments_data/'
     
const fetchDepartmentData = async () => {
    try {
      const response = await fetch(departmentsData_url);

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();

      return data;

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

export default fetchDepartmentData;