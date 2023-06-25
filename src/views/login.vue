<template>
  <div style="margin-top: 20%;">
    <p>账号：<input type="text" v-model="username" /></p>
    <p>密码：<input type="password" v-model="password" /></p>
    <p><button @click="login" style="margin-left: 3%;">登录</button></p>
  </div>
  <div class="tabulation1">
    <div
      class="register"
      :style="{ width: fullWidth + 'px', height: fullHeight + 'px' }"
    >
      <div class="img_box1" :style="{ width: fullWidth + 'px' }"></div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      user: "",
      pwd: "",
      fullWidth: document.documentElement.clientWidth,
      fullHeight: document.documentElement.clientHeight,
    };
  },
  beforeUpdate() {
    this.onRefresh();
  },
  methods: {
    handleResize() {
      this.fullWidth = document.documentElement.clientWidth;
      this.fullHeight = document.documentElement.clientHeight;
    },
    login() {
      Axios.post("/user/login/", {
        username: this.username,
        password: this.password,
      })
        .then((resp) => {
          console.log(resp.data);
          if (resp.data.code == 200) {
            localStorage.setItem("username", resp.data.username);
            localStorage.setItem("user_id", resp.data.user_id);
            localStorage.setItem("token", resp.data.token);
            this.$router.push("/main_page");
          } else {
            alert(resp.data.msg);
          }
        })
        .catch((err) => {
          alert("账号/密码错误");
          console.log(err);
        });
    },
  },
  created() {
    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
};
</script>

<style  scoped>
#slide-verify-slider {
  position: relative;
  text-align: center;
  width: 100%;
  height: 40px;
  line-height: 40px;
  margin-top: 15px;
  background: #f7f9fa;
  color: #45494c;
  border: 1px solid #e4e7eb;
}
#box-title {
  margin-top: 80px;
}
.img_box1 {
  position: absolute;
  background-image: url(../utils/img/login.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  width: 101%;
  height: 101%;
}
</style>
