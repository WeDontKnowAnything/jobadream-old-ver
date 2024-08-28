import { http } from '@/api/http'

export function getPostList() {
  return http.get('/api/v1/boards')
}

export function getPost(id: any) {
  return http.get('/api/v1/posts', { params: { post_id: id } })
}

export function addPost(data: any) {
  return http.post('/api/v1/posts', data)
}

export function getComments(id: any) {
  return http.get('/api/v1/posts/comments', { params: { post_id: id } })
}

export function addComment(data: any) {
  return http.post('/api/v1/post/comments', data)
}
