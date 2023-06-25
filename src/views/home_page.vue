<template>
  <div>
    <div class="tabulation5">佳音网络</div>
    <div class="tabulation3"></div>
    <div class="tabulation2">
      <a href="http://www.szgymz.com/">首页</a
      ><span class="itemSepLine"
        >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span
      >
      <a href="http://www.szgymz.com/">关于我们</a
      ><span class="itemSepLine"
        >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span
      >
      <a href="http://www.szgymz.com/">核心业务</a
      ><span class="itemSepLine"
        >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span
      >
      <a href="http://www.szgymz.com/">新闻动态</a
      ><span class="itemSepLine"
        >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span
      >
      <!-- <button style="width: 100px; height: 50px" @click="addlogin()"> -->
      <el-button type="primary" round @click="addlogin()">登录</el-button>
      <!-- </button> -->
    </div>

    <div class="tabulation1">
      <div
        class="register"
        :style="{ width: fullWidth + 'px', height: fullHeight + 'px' }"
      >
        <div class="img_box" :style="{ width: fullWidth + 'px' }"></div>
      </div>
    </div>
    <div class="buttom">
      <i style="font-family: math; color: white">公司内容</i>
    </div>
    <div class="line"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      is_show: true,
      viisibale: false,
      username: "",
      password: "",
      fullWidth: document.documentElement.clientWidth,
      fullHeight: document.documentElement.clientHeight,
    };
  },
  methods: {
    addlogin() {
      this.$router.push({
        path: "/login",
      });
    },
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

<style>
.tabulation2 {
  height: 50px;
  width: 51%;
  position: absolute;
  background: rgb(249, 250, 251);
  left: 49%;
}
.tabulation5 {
  width: 10%;
  height: 50px;
  position: absolute;
  background: rgb(249, 250, 251);
}
.tabulation3 {
  width: 40%;
  height: 50px;
  left: 9%;
  position: absolute;
  background: rgb(249, 250, 251);
}
.itemSepLine {
  width: 20px;
}
.register {
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}
.img_box {
  position: absolute;
  background-image: url(../utils//img/aaa123.png);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  width: 101%;
  height: 101%;
}
.buttom {
  position: absolute;
  top: 90%;
  width: 100%;
  height: 150px;
}
.line {
  float: right;
  width: 100%;
  height: 1px;
  margin-top: 42em;
  background: #67e9a3;
  position: relative;
  text-align: center;
}
</style>