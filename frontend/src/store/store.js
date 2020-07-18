import Vue from 'vue'
import { firebaseAuth, firebaseDb } from 'boot/firebase'

const state = {
	userDetails: {},
	users: {},
	error_message: null
}

const mutations = {
	setUserDetails(state, payload) {
		state.userDetails = payload
	},
	addUser(state, payload) {
		Vue.set(state.users, payload.userId, payload.userDetails)
	},
	updateUser(state, payload) {
		Object.assign(state.users[payload.userId], payload.userDetails)
	},
	setErrorMessage(state, payload) {
		state.error_message = payload
	}
}

const actions = {
	registerUser({}, payload) {
		firebaseAuth.createUserWithEmailAndPassword(payload.email, payload.password)
			.then(response => {
				console.log(response)
				let userId = firebaseAuth.currentUser.uid
				firebaseDb.ref('users/' + userId).set({
                    name: payload.name,
					phone_no: payload.phone_no,
                    email: payload.email,
                    user_type: payload.user_type,
					online: true
				})
			})
			.catch(error => {
				console.log(error.message)
			})
	},
	loginUser({}, payload) {
		firebaseAuth.signInWithEmailAndPassword(payload.email, payload.password)
			.then(response => {
				console.log(response)
			})
			.catch(error => {
				console.log(error.message)
				commit('setErrorMessage', error.message)
			})		
	},
	logoutUser() {
		firebaseAuth.signOut()
    },
    handleAuthStateChanged({ commit, dispatch, state }) {
		firebaseAuth.onAuthStateChanged(user => {
		  if (user) {
		    // User is logged in.
		    let userId = firebaseAuth.currentUser.uid
		    firebaseDb.ref('users/' + userId).once('value', snapshot => {
		    	let userDetails = snapshot.val()
		    	commit('setUserDetails', {
                    name: userDetails.name,
                    phone_no: userDetails.phone_no, 
		    		email: userDetails.email,                  
		    		user_type: userDetails.user_type,
		    		userId: userId
		    	})
		    })
		    dispatch('firebaseUpdateUser', {
		    	userId: userId,
		    	updates: {
		    		online: true
		    	}
		    })
		    dispatch('firebaseGetUsers')
		    this.$router.push('/')
		  }
		  else {
		  	// User is logged out.
		  	dispatch('firebaseUpdateUser', {
		  		userId: state.userDetails.userId,
		  		updates: {
		  			online: false
		  		}
		  	})
		  	commit('setUserDetails', {})
		  	this.$router.replace('/auth-login')
		  }
		})
	},

	firebaseUpdateUser({}, payload) {
		if (payload.userId) {
			firebaseDb.ref('users/' + payload.userId).update(payload.updates)
		}
	},
	firebaseGetUsers({ commit }) {
		firebaseDb.ref('users').on('child_added', snapshot => {
			let userDetails = snapshot.val()
			let userId = snapshot.key
			commit('addUser', {
				userId,
				userDetails
			})
		})
		firebaseDb.ref('users').on('child_changed', snapshot => {
			let userDetails = snapshot.val()
			let userId = snapshot.key
			commit('updateUser', {
				userId,
				userDetails
			})
		})
	},
}

const getters = {
    getUserDetails: state => {
		return state.userDetails
	},
	errorMessage: state => {
		return state.error_message
	}
}

export default {
	namespaced: true,
	state,
	mutations,
	actions,
	getters
}