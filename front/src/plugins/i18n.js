import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

const messages = {
    en: {
        about_us: 'About us',
        address: 'Address',
        add_email: 'Add your email address here',
        copyright: 'Copyright',
        contact: 'Contact us',
        home: 'Home',
        information: 'Informations',
        login: 'Login',
        press: 'Press',
        search: 'Search',
        signup: 'Signup',
        send: 'Send',
        terms_of_use: 'Terms of use',
        testimony: 'Testimony | Testimonies',
        message: {
        }
    },
    
    fr: {
        about_us: 'À propos',
        address: 'Adresse',
        add_email: 'Ajouter votre email ici',
        copyright: 'Tous droits réservés',
        contact: 'Contact',
        home: 'Accueil',
        information: 'Information',
        login: 'Connexion',
        press: 'Presse',
        search: 'Rechercher',
        signup: 'Inscription',
        send: 'Envoyer',
        terms_of_use: "Conditions d'uttilisation",
        testimony: 'Témoignage | Témoignages',
        message: {
        }
    }
}

const i18n = new VueI18n({
    locale: 'en',
    fallbackLocale: 'en',
    localeDir: 'locales',
    messages
})

export default i18n
