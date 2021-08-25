using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class Screnshot : MonoBehaviour
{
#if UNITY_EDITOR
    [SerializeField] private KeyCode keyCode;
    [SerializeField] private string pathFile;

    private string pathAsset = null;
    private int indexScreenshot = 0;
    private List<string> nameScreenshot = new List<string>();

    private void Start()
    {
        pathAsset = Application.dataPath.Replace("/Assets", "");
    }

    private void Update()
    {
        if (Input.GetKeyDown(keyCode))
        {
            ScreenCapture.CaptureScreenshot($"Screenshot_{indexScreenshot}.png");
            nameScreenshot.Add($"Screenshot_{indexScreenshot}.png");
            indexScreenshot++;
        }
    }

    private void OnApplicationQuit()
    {
        string datePath = DateTime.Now.ToString().Replace(" ", "\\").Replace(":", ".");

        Directory.CreateDirectory($"{pathFile}\\{datePath}");
        pathFile = $"{pathFile}\\{datePath}";

        foreach (var item in nameScreenshot)
            File.Move($"{pathAsset}/{item}", $"{pathFile}/{item}");

    }
#endif
}
