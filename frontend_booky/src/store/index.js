import { createStore } from 'vuex';

export default createStore({
  state: {
    user: {
      token: '',
      isAuthenticated: false,
    },
  },
  mutations: {
    initializeStore(state) {
      const token = localStorage.getItem('token');
      if (token) {
        state.user.token = token;
        state.user.isAuthenticated = true;
      } else {
        state.user.token = '';
        state.user.isAuthenticated = false;
      }
    },
    setToken(state, token) {
      state.user.token = token;
      state.user.isAuthenticated = true;
      localStorage.setItem('token', token);
    },
    removeToken(state) {
      state.user.token = '';
      state.user.isAuthenticated = false;
      localStorage.removeItem('token');
    },
  },
  actions: {},
  modules: {},
});
