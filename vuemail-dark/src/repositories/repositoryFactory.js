import NotesRepository from './notesRepository'

const repositories = {
  notes: NotesRepository
}

export const RepositoryFactory = {
  get: function(name) {
    return repositories[name]
  }
}
