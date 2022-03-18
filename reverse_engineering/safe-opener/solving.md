 1. Download the javafile
 1. look at the base64 string

```java
public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
```

 1. Just decode the base64 string 

```shell
echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
```
 1. You have your flag
