import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.blue, // Set the background color to blue
        body: Center(
          child: Text(
            'Hello, World!',
            style:
                TextStyle(color: Colors.white), // Text color white for contrast
          ),
        ),
      ),
    );
  }
}
