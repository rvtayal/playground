using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBehavior : MonoBehaviour
{

    public Camera playerCam;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Debug.Log("Mouse Clicked");
            Ray ray = new Ray(playerCam.transform.position, playerCam.transform.forward);
            RaycastHit hit;
            Debug.DrawRay(transform.position, ray.direction * 50f);
            if (Physics.Raycast(ray, out hit, 50.0f))
            {
                Debug.Log("Object hit");
                // Debug.Log(hit.collider.gameObject.tag);
                if (hit.collider.gameObject.tag == "Active")
                {
                    Debug.Log("Active Object Hit");
                    hit.collider.gameObject.GetComponent<DoorBehavior>().Activate();
                }
            }
        }
    }
}
