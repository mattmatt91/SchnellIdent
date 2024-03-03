
const localIpAddress = "192.168.1.2";


export async function getMeasurement() {
    const response = await fetch(`http://${localIpAddress}:4000/measurement`, { mode: 'cors' });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  }
  
export async function getAllIds() {

    const response = await fetch(`http://${localIpAddress}:4000/get_all_ids`, { mode: 'cors' });
    console.log(response)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  }
  


  export async function getMeasurementById(selectedId) {
    if (!selectedId) {
      throw new Error('Selected ID is required');
    }
    const response = await fetch(`http://${localIpAddress}:4000/get_measurement/${selectedId}`, { mode: 'cors' });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parses the JSON body of the response
}