import axios from 'axios'

const BaseURL: string = location.host.split(':')[0]
const Port = 8000

const http = axios.create({ baseURL: `http://${BaseURL}:${Port}` })

export { http }
