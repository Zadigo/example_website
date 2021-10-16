<script>
import { BModal } from 'bootstrap-vue'

export default {
  name: 'ExtendedModal',
  extends: BModal,
  props: {
      positionX: {
          type: String,
          default: null
      },
      positionY: {
        type: String,
        default: null
      },
      fullScreen: Boolean
  },

  mounted() {
    if (this.isPositionedY) {
      this.$refs.content.classList.add('rounded-0')
    }
  },
  
  computed: {
    modalClasses() {
      return [
        {
          fade: !this.noFade,
          show: this.isShow
        },
        this.positionX,
        this.positionY,
        this.modalClass
      ]
    },

    dialogClasses() {
      var positionClasses = {
        'modal-fullscreen': this.fullScreen,
        'modal-frame': this.isPositionedY && !this.isPositionedX,
        'modal-side': this.isPositionedX && !this.fullScreen
      }

      var position = 'modal-'

      if (this.isPositionedY & !this.fullScreen) {
        position = position + this.positionY
      }

      if (this.isPositionedX & !this.fullScreen) {
        position = position + '-' + this.positionX
      }

      if (this.isPositioned) {
        positionClasses[position] = true
      }
      
      return [
        {
          [`modal-${this.size}`]: this.size,
          'modal-dialog-centered': this.centered,
          'modal-dialog-scrollable': this.scrollable
        },
        positionClasses,
        this.dialogClass
      ]
    },

    isPositionedX() {
      return this.positionX === 'left' | this.positionX === 'right' ? true : false
    },

    isPositionedY() {
      return this.positionY === 'top' | this.positionY === 'bottom' ? true : false
    },

    isPositioned() {
      return [this.isPositionedX, this.isPositionedY].some((x) => { return x === true })
    },

    getPositionY() {
      if (this.positionY == null) {
        return 'top'
      } else {
        return this.positionY
      }
    }
  }
}
</script>
