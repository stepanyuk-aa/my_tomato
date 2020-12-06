import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:async/async.dart';
import 'tasks.dart';

class Window_auth extends StatelessWidget {
  final _sizeTextBlack = const TextStyle(fontSize: 20.0, color: Colors.black);
  final _sizeTextWhite = const TextStyle(fontSize: 20.0, color: Colors.white);

  final TextEditingController login = new TextEditingController(text: 'admin');
  final TextEditingController password = new TextEditingController(text: 'Skill39!');

  @override
    Widget build(BuildContext context) {
      return Scaffold(
      appBar: AppBar(title: Text('Авторизация')),
      body: new Scaffold(
          body: new Center(
              child: new Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  new Container(
                    child: new TextFormField(
                      decoration: new InputDecoration(labelText: "Email"),
                      controller: login,
                      keyboardType: TextInputType.emailAddress,
                      style: _sizeTextBlack,
                    ),
                    width: 400.0,
                  ),
                  new Container(
                    child: new TextFormField(
                      decoration: new InputDecoration(labelText: "Password"),
                      controller: password,
                      obscureText: true,
                      style: _sizeTextBlack,
                    ),
                    width: 400.0,
                    padding: new EdgeInsets.only(top: 10.0),
                  ),
                  new Padding(
                    padding: new EdgeInsets.only(top: 25.0),
                    child: new RaisedButton(
                      color: Colors.red,
                      onPressed: () async {
                        var ip = '192.168.1.105:5000';
                        var url = 'http://$ip/login';

                        print("Create request to $url");

                        Response response;
                        Dio dio = new Dio();
                        response = await dio.post(url, data: {'login': login.text, 'password': password.text});
                        var token = response.data['token'];

                        if (response.data['status'] == 'success'){
                          print('OKOKOKOKOK');

                          Response response;
                          Dio dio = new Dio();
                          var url = 'http://$ip/gettasks';
                          response = await dio.post(url, data: {'token': token});

                          Navigator.push(context, MaterialPageRoute(builder: (context) => Window_tasks(text: token, tasks:response.data)));
                        }
                        else {
                          var url = 'http://$ip/gettasks';
                          print("Create get_tasks request to $url");

                          Navigator.push(context, MaterialPageRoute(builder: (context) => AllertLogin()));
                        }
                      },
                      child: new Text(
                        "Войти",
                        style: _sizeTextWhite,
                      ),
                    ),
                  )
                ],
              )
          )
      )
    );
  }
}

class AllertLogin extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text('Такой комбинации логин/пароль нет в базе'),
      actions: [
        FlatButton(
          onPressed: () {Navigator.pop(context);},
          child: Text('Исправлюсь'),
        ),
      ],
    );
  }
}