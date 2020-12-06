import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:async/async.dart';


class Window_tasks extends StatelessWidget {
  final _sizeTextBlack = const TextStyle(fontSize: 20.0, color: Colors.black);
  final _sizeTextWhite = const TextStyle(fontSize: 20.0, color: Colors.white);

  final String text;
  final List tasks;
  Window_tasks({Key key, @required this.text, this.tasks}) : super(key: key);

  var list = ["one", "two", "three", "four"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text('Задачи')),
        body: new Scaffold(
            body: new RaisedButton(
              color: Colors.red,
              // onPressed: test,
              child: Center(
                child: Column(
                  children:
                    <Widget>[
                      for(var task in tasks ) Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          for(var item in task ) Text(item.toString() + '\t')
                        ],
                      ),
                    ],
                ),
              )
        ),
          )
    );
  }
}