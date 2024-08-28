import { http } from '@/api/http'

export function getJobList() {
  return http.get('/api/v1/jobs')
}

export function getJob(id: any) {
  return http.get('/api/v1/job', { params: { job_id: id } })
}
