import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

export function updateLoan(loan, jwt) {
  return axios.put(`${API_URL}/loans/edit/${loan.id}/`, loan, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchAllLoans(jwt) {
  return axios.get(`${API_URL}/loans/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchLoan(loanId, jwt) {
  return axios.get(`${API_URL}/loans/${loanId}/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function downloadFile(filename, folder, jwt) {
  return axios.get(`${API_URL}/loans/download/${folder}/${filename}/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function fetchLoans(userId, jwt) {
  return axios.get(`${API_URL}/loans/user/${userId}/`, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function postLoan(loan, jwt) {
  return axios.post(`${API_URL}/loans/`, loan, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function uploadProfilePhoto(image, userId, jwt) {
  return axios.put(`${API_URL}/users/upload/photo/${userId}/`, image, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function updateUser(user, userId, jwt) {
  return axios.put(`${API_URL}/users/${userId}/`, user, {
    headers: { Authorization: `Bearer: ${jwt}` },
  });
}

export function login(user) {
  return axios.post(`${API_URL}/users/login/`, user);
}

export function register(user) {
  return axios.post(`${API_URL}/users/register/`, user);
}
