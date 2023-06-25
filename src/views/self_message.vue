<template>
  <div>
    <el-button type="text" disabled>{{ username }}</el-button>
  </div>
  <div><el-button type="text" @click="tanchuang">修改密码</el-button></div>
  <div
    v-show="is_show"
    class="show"
    style="
      padding-top: 30%;
      font-size: 20px;
      width: 50%;
      background-color: rgb(193, 130, 130);
      margin-left: 25%;
      margin-top: -2%;
    "
  >
    <div class="close" style="margin-left: 92%; margin-top: -60%">
      <el-button type="danger" round @click="cancel">
        <b class="el-icon-close"> </b>
      </el-button>
      <div class="name" style="margin-top: -2%;width: 170%;">用户名：</div>
      <div class="user" style="margin-right: -270%;margin-left: -70%;margin-top: -45%;"><el-input v-model="username" :disabled="true"></el-input></div>
      <div class="pass" style="margin-top: 50%;width: 170%;">密码：</div>
      <div class="pwd" style="margin-right: -270%;margin-left: -70%;margin-top: -45%;"><el-input placeholder="请输入密码" v-model="password" show-password></el-input></div>
      <div class="van_button" style="margin-top: 45%;width: 200%;"><van-button color="linear-gradient(to right, #ff6034, #ee0a24)" @click="check_password">确认修改</van-button></div> 
    </div>
  </div>
  <div>
    <el-button type="danger" round @click="logout">退出登录</el-button>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      username: localStorage.getItem("username"),
      input: "",
      is_show: false,
      input: '',
      password: '',
    };
  },
  methods: {
    logout() {
      Axios.get("/user/logout/")
        .then((resp) => {
          console.log(resp.data);
          if (resp.data.code == 200) {
            localStorage.removeItem("token");
            localStorage.removeItem("user_id");
            localStorage.removeItem("username");
            this.$router.push("/");
          } else {
            alert(resp.msg);
          }
        })
        .catch((err) => {
          alert("执行错误");
          console.log(err);
        });
    },
    check_password() {
      Axios.post("/user/put_pass/", {
        username: this.username,
        password: this.password,
      })
        .then((resp) => {
          console.log(resp.data);
          if (resp.data.code == 200) {
            localStorage.setItem("username", resp.data.username);
            localStorage.setItem("user_id", resp.data.user_id);
            localStorage.setItem("token", resp.data.token);
            // this.$router.push("/main_page");
            alert('修改成功')
            this.cancel()
          }else{
            alert(resp.data.msg);
          }
        })
        .catch((err) => {
          alert("账号/密码错误");
          console.log(err);
        });
    },
    tanchuang() {
      this.is_show = true;
    },
    cancel() {
      this.is_show = false;
    },
  },
};
</script>

<style>
.show {
  position: relative;
}
.close {
  position: relative;
}
.user{
    position: relative; 
    right: 670%;
}
.name{
    position: relative; 
    left: -905%;
}
.pass{
    position: relative; 
    left: -888%;
}
.pwd{
    position: relative; 
    left: -668%;
}
.van_button{
    position: relative; 
    left: -640%;
}
</style>