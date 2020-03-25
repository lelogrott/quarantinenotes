import Repository from './repository'

const resource = '/notes'
export default {
  get() {
    return Repository.get();
  },
  getNote(noteId) {
    return Repository.get(`${resource}/${noteId}`);
  },
  createNote(payload) {
    return Repository.post(`${resource}`, payload);
  }
}
