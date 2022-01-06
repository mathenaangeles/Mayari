import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

export function fetchLoans(userId, jwt) {
  return axios.get(`${API_URL}/loans/${userId}`, { headers:{ Authorization: `Bearer: ${jwt}`} })
}

export function fetchLoan (loanId, jwt) {
  return axios.get(`${API_URL}/loans/${loanId}/`, { headers:{ Authorization: `Bearer: ${jwt}`} })
}

export function postLoan (loan, jwt) {
  return axios.post(`${API_URL}/surveys/`, loan, { headers: { Authorization: `Bearer: ${jwt}` } })
}

export function login(user) {
  return axios.post(`${API_URL}/users/login/`, user);
}

export function register(user) {
  return axios.post(`${API_URL}/users/register/`, user);
}
