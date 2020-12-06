import 'package:flutter/material.dart';
import 'package:flutter_app/tasks.dart';
import 'auth.dart';

void main() {
  runApp(
    MaterialApp(
      routes: {
        '/':(BuildContext context) => Window_auth(),
        '/tasks':(BuildContext context) => Window_tasks()
      },
    )
  );
}

