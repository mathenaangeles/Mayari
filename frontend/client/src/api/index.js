import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export function fetchLoans() {
  return axios.get(`${API_URL}/loans/`, {headers:{ Authorization: `Bearer: ${jwt}`}})
}

export function login(userData) {
  return axios.post(`${API_URL}/login/`, userData)
}

export function register(userData) {
  return axios.post(`${API_URL}/register/`, userData)
}