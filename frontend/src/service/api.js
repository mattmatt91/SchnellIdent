
const localIpAddress = "localhost";


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

export async function deleteMeasurementById(measurementId) {
  if (!measurementId) {
    throw new Error('Measurement ID is required');
  }
  const response = await fetch(`http://${localIpAddress}:4000/delete_measurement/${measurementId}`, {
    method: 'GET',
    mode: 'cors'
  });
  if (!response.ok) {
    throw new Error('Network response was not ok');
  } 
  return await response.json();
}

export async function downloadMeasurementById(measurementId) {
  if (!measurementId) {
    throw new Error('Measurement ID is required');
  }
  const response = await fetch(`http://${localIpAddress}:4000/download_measurement/${measurementId}`, { 
    method: 'GET', 
    mode: 'cors' 
  });
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  // Handling the response as a Blob for file download
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.style.display = 'none';
  a.href = url;
  a.download = `measurement_${measurementId}.zip`; // Adjust the file extension as needed
  document.body.appendChild(a);
  a.click();
  window.URL.revokeObjectURL(url);
}


export async function downloadAllMeasurements() {
  const response = await fetch(`http://${localIpAddress}:4000/download_all_measurements`, { 
    method: 'GET', 
    mode: 'cors' 
  });
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  // Handling the response as a Blob for file download
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.style.display = 'none';
  a.href = url;
  a.download = `all_measurements.zip`; // Adjust the file extension as needed
  document.body.appendChild(a);
  a.click();
  window.URL.revokeObjectURL(url);
}
